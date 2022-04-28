from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from University_Faculty.classroom.forms import StudentInterestForm
from University_Faculty.classroom.models import Student, Quiz, Result, Question
from University_Faculty.common.constants import OPTIONS_MAPPER

from University_Faculty.common.decorators import student_required
from University_Faculty.common.helpers import is_ajax


@method_decorator([login_required, student_required], name='dispatch')
class QuizListView(views.ListView):
    model = Quiz
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'classroom/students_quiz_list.html'

    def get_queryset(self):
        student = self.request.user.student
        student_interest = student.interests.all()
        res = Result.objects.filter(student=self.request.user).values_list('quiz', flat=True)
        queryset = Quiz.objects \
            .filter(subject__in=student_interest) \
            .annotate(questions_count=Count('questions')) \
            .filter(questions_count__gte=5) \
            .exclude(id__in=res)

        queryset = queryset
        return queryset


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestView(views.UpdateView):
    model = Student
    template_name = 'classroom/interest_form.html'
    form_class = StudentInterestForm
    success_url = reverse_lazy('student quizzes')

    def get_object(self, queryset=None):
        return self.request.user.student


@login_required
@student_required
def take_quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    context = {
        'quiz': quiz,
    }
    return render(request, 'classroom/quiz.html', context)


@login_required
@student_required
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    questions_pks = {}
    for q in quiz.get_questions():
        options = [q.option_1, q.option_2, q.option_3, q.option_4]
        questions.append({str(q): options})

    for q in quiz.get_questions():
        questions_pks[str(q)] = q.pk

    context = {
        'data_pk': questions_pks,
        'data': questions,
        'time': quiz.time,
    }
    return JsonResponse(context)


@login_required
@student_required
def quiz_save_view(request, pk):
    if is_ajax(request):
        questions = []
        results = []
        data = request.POST

        data = dict(data.lists())
        data.pop('csrfmiddlewaretoken')

        for k in data.keys():
            question = Question.objects.get(pk=k)
            questions.append(question)

        student = request.user
        quiz = Quiz.objects.get(pk=pk)
        score = 0
        max_score = quiz.max_score
        multiplier = max_score / len(questions)
        for q in questions:

            options = [q.option_1, q.option_2, q.option_3, q.option_4]

            selected_option = request.POST.get(str(q.pk))

            if selected_option not in options:
                results.append({str(q): 'not answered'})
                continue

            for i in range(len(options)):
                current = options[i]
                if current == selected_option:
                    answer = OPTIONS_MAPPER[i]
                    results.append({str(q): {'correct_option': q.correct_option, 'selected': answer}})
                    if answer == q.correct_option:
                        score += 1
                        break

        score = score * multiplier

        try:
            result = Result.objects.get(student=student, quiz=quiz)
            if result.score < score:
                result.score = score
                result.save()
        except Result.DoesNotExist:
            Result.objects.create(student=student, quiz=quiz, score=score)

        passed = False

        if score >= quiz.required_score_to_pass:
            passed = True

        context = {
            'passed': passed,
            'score': score,
            'results': results,
            'max_score': max_score,
        }

        return JsonResponse(context)


@method_decorator([login_required, student_required], name='dispatch')
class QuizTakenListView(views.ListView):
    model = Result
    template_name = 'classroom/student_quiz_taken.html'

    # get only users quizzes from the database
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taken_quizzes'] = Result.objects.filter(student=self.request.user)
        return context

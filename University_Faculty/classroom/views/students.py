from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.classroom.forms import StudentInterestForm
from University_Faculty.classroom.models import Student, Quiz, Result, Question
from University_Faculty.common.constants import OPTIONS_MAPPER
from University_Faculty.common.decorators import student_required
from University_Faculty.common.helpers import is_ajax


class StudentInterestView(views.UpdateView):
    model = Student
    template_name = 'classroom/interest_form.html'
    form_class = StudentInterestForm
    success_url = reverse_lazy('quizzes')

    def get_object(self, queryset=None):
        return self.request.user.student


def take_quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    context = {
        'quiz': quiz,
    }
    return render(request, 'classroom/quiz.html', context)


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []

    for q in quiz.get_questions():
        options = [q.option_1, q.option_2, q.option_3, q.option_4]
        questions.append({str(q): options})

    context = {
        'data': questions,
        'time': quiz.time,
    }
    return JsonResponse(context)


def quiz_save_view(request, pk):
    if is_ajax(request):
        questions = []
        results = []
        data = request.POST
        data = dict(data.lists())
        data.pop('csrfmiddlewaretoken')

        for k in data.keys():
            question = Question.objects.get(question=k)
            questions.append(question)

        student = request.user
        quiz = Quiz.objects.get(pk=pk)
        score = 0
        multiplier = quiz.max_score / len(questions)
        for q in questions:

            options = [q.option_1, q.option_2, q.option_3, q.option_4, '']

            selected_option = request.POST.get(q.question)
            selected_option = options.index(selected_option)
            selected_option = OPTIONS_MAPPER[selected_option]

            if selected_option != "":
                correct_option = q.correct_option
                if selected_option == correct_option:
                    score += 1
                results.append({str(q): {'correct_option': q.correct_option, 'selected': selected_option}})
            else:
                results.append({str(q): 'not answered'})

        score = score * multiplier
        Result.objects.create(student=student, quiz=quiz, score=score)
        passed = False

        if score >= quiz.required_score_to_pass:
            passed = True

        context = {
            'passed': passed,
            'score': score,
            'results': results,
        }

        return JsonResponse(context)


class QuizTakenListView(views.ListView):
    model = Quiz
    template_name = 'classroom/student_quiz_taken.html'
    context_object_name = 'taken_quiz'

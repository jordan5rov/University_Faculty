from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from University_Faculty.classroom.forms import TeacherEditQuizForm
from University_Faculty.classroom.models import Quiz, Result
from University_Faculty.classroom.views.authentication import RegisterView
from University_Faculty.common.decorators import teacher_required


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizListView(views.ListView):
    model = Quiz
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'classroom/teachers_quiz_list.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject') \
            .annotate(questions_count=Count('questions', distinct=True))
        return queryset


class QuizCreateView(views.CreateView):
    model = Quiz
    fields = ('name', 'subject', 'time', 'required_score_to_pass', 'max_score')
    template_name = 'classroom/quiz_create.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.save()
        return redirect('teacher quizzes')


class QuizUpdateView(views.UpdateView):
    model = Quiz
    form_class = TeacherEditQuizForm
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_update.html'

    def get_context_data(self, **kwargs):
        kwargs['questions'] = self.get_object().questions.annotate(answers_count=Count('correct_option'))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.request.user.quizzes.all()

    def get_success_url(self):
        return reverse_lazy('teacher quizzes')


class QuizDeleteView(views.DeleteView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_delete_confirm.html'
    success_url = reverse_lazy('teacher quizzes')

    def get_queryset(self):
        return self.request.user.quizzes.all()


class QuizResultsView(views.DetailView):
    model = Result
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result_list = Result.objects.filter(quiz=self.get_object())

        context['total_taken'] = result_list.count()

        scores = [result.score for result in result_list]
        if len(scores):
            context['average_score'] = sum(scores) / len(scores)

        context['results'] = result_list

        return context

    def get_queryset(self):
        return self.request.user.quizzes.all()

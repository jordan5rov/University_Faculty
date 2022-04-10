from django.db.models import Count, Avg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from University_Faculty.classroom.models import Quiz


class QuizListView(views.ListView):
    model = Quiz
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'classroom/quiz_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Quiz.objects.all()
        return queryset


class QuizCreateView(views.CreateView):
    model = Quiz
    fields = ('name', 'subject',)
    template_name = 'classroom/quiz_create.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.save()
        return redirect('quizzes')


class QuizUpdateView(views.UpdateView):
    model = Quiz
    fields = ('name', 'subject',)
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_update.html'

    def get_context_data(self, **kwargs):
        kwargs['questions'] = self.get_object().questions.annotate(answers_count=Count('correct_option'))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.request.user.quizzes.all()

    def get_success_url(self):
        return reverse_lazy('quizzes')


class QuizDeleteView(views.DeleteView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_delete_confirm.html'
    success_url = reverse_lazy('quizzes')

    def get_queryset(self):
        return self.request.user.quizzes.all()


class QuizResultsView(views.DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/quiz_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        taken_quizzes = quiz.taken_quizzes.select_related('student__user').order_by('-date')

        total_taken_quizzes = taken_quizzes.count()
        quiz_score = quiz.taken_quizzes.aggregate(average_score=Avg('score'))
        context['taken_quizzes'] = taken_quizzes
        context['total_taken_quizzes'] = total_taken_quizzes
        context['quiz_score'] = quiz_score

        return context

    def get_queryset(self):
        return self.request.user.quizzes.all()

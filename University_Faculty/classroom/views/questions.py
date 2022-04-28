from pyexpat import model

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from University_Faculty.classroom.forms import QuestionForm
from University_Faculty.classroom.models import Quiz, Question
from University_Faculty.common.decorators import teacher_required


@login_required
@teacher_required
def create_question_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('update quiz', quiz.pk)
    else:
        form = QuestionForm(request.GET)

    context = {
        'quiz': quiz,
        'form': form
    }

    return render(request, 'classroom/question_create.html', context)


@login_required
@teacher_required
def edit_question_view(request, quiz_pk, question_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk, owner=request.user)
    question = get_object_or_404(Question, pk=question_pk, quiz=quiz)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('update quiz', quiz.pk)
    else:
        form = QuestionForm(instance=question)

    context = {
        'quiz': quiz,
        'question': question,
        'form': form,
    }
    return render(request, 'classroom/question_update.html', context)


@method_decorator([login_required, teacher_required], name='dispatch')
class QuestionDeleteView(views.DeleteView):
    model = Question
    template_name = 'classroom/question_delete_confirm.html'
    pk_url_kwarg = 'question_pk'

    def get_context_data(self, **kwargs):
        question = self.get_object()
        kwargs['quiz'] = question.quiz
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Question.objects.filter(quiz__owner=self.request.user)

    def get_success_url(self):
        question = self.get_object()
        return reverse_lazy('update quiz', kwargs={'pk': question.quiz_id})

from pyexpat import model

from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.classroom.forms import QuestionForm, BaseAnswerInlineFormSet
from University_Faculty.classroom.models import Quiz, Question, StudentAnswer


def create_question_view(request, pk):
    # By filtering the quiz by the url keyword argument `pk` and
    # by the owner, which is the logged in user, we are protecting
    # this view at the object-level. Meaning only the owner of
    # quiz will be able to add questions to it.
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

    return render(request, 'classroom/question_create.html', {'quiz': quiz, 'form': form})


def edit_question_view(request, quiz_pk, question_pk):
    # Simlar to the `question_add` view, this view is also managing
    # the permissions at object-level. By querying both `quiz` and
    # `question` we are making sure only the owner of the quiz can
    # change its details and also only questions that belongs to this
    # specific quiz can be changed via this url (in cases where the
    # user might have forged/player with the url params.
    quiz = get_object_or_404(Quiz, pk=quiz_pk, owner=request.user)
    question = get_object_or_404(Question, pk=question_pk, quiz=quiz)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('result quiz', quiz.pk)
    else:
        form = QuestionForm(instance=question)

    return render(request, 'classroom/question_update.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
    })


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

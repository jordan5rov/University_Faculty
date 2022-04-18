from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.classroom.forms import StudentInterestForm
from University_Faculty.classroom.models import Student, Quiz, Result
from University_Faculty.common.decorators import student_required


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
        answers = [q.option_1, q.option_2, q.option_3, q.option_4]
        questions.append({str(q): answers})

    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

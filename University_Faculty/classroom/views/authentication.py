from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.classroom.forms import StudentCreateForm, TeacherCreateForm
from University_Faculty.classroom.models import Student


class RegisterView(views.TemplateView):
    template_name = 'classroom/register.html'


class StudentRegisterView(views.CreateView):
    template_name = 'classroom/register_form.html'
    model = Student
    form_class = StudentCreateForm
    # student quiz list
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return user


class TeacherRegisterView(views.CreateView):
    template_name = 'classroom/register_form.html'
    model = get_user_model()
    form_class = TeacherCreateForm
    # teacher quiz list
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return user

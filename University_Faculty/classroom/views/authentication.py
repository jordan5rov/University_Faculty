from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

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


class TeacherRegisterView(views.CreateView):
    template_name = 'classroom/register_form.html'
    model = get_user_model()
    form_class = TeacherCreateForm
    # teacher quiz list
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)


class LoginView(auth_views.LoginView):
    template_name = 'classroom/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.request.user:
            return self.success_url
        return super().get_success_url()


class LogoutView(auth_views.LogoutView):
    next_page = 'home'

from django.contrib.auth import mixins as auth_mixins, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.accounts.forms import CreateStudentForm
from University_Faculty.common.view_mixins import RedirectToHome


class StudentRegisterView(RedirectToHome, views.CreateView):
    form_class = CreateStudentForm
    template_name = 'accounts/student_register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/student_login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

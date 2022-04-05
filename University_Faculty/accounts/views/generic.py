from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views


class UserRegisterView(views.TemplateView):
    template_name = 'accounts/register.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

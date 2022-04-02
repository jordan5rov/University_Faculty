from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views


class RegisterView(views.TemplateView):
    template_name = 'accounts/register.html'


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from University_Faculty.accounts.forms import CreateTeacherForm
from University_Faculty.accounts.models import UniversityUser
from University_Faculty.common.view_mixins import RedirectToHome


class TeacherRegisterView(RedirectToHome, views.CreateView):
    model = UniversityUser
    form_class = CreateTeacherForm
    template_name = 'accounts/teacher_register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


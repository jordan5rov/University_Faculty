from django.contrib.auth import mixins as auth_mixins, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.accounts.forms import CreateStudentForm
from University_Faculty.accounts.models import UniversityUser
from University_Faculty.common.view_mixins import RedirectToHome


class StudentRegisterView(RedirectToHome, views.CreateView):
    model = UniversityUser
    form_class = CreateStudentForm
    template_name = 'accounts/student_register.html'
    success_url = reverse_lazy('home')

    def get_context_fata(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result




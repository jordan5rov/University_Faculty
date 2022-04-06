from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views import generic as views

from University_Faculty.accounts.models import Student
from University_Faculty.common.decorators import student_required
from University_Faculty.exam.forms import StudentInterestForm
from University_Faculty.exam.models import Exam


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestsView(views.TemplateView):
    model = Student
    template_name = 'exam/interest_form.html'
    form_class = StudentInterestForm


@method_decorator([login_required, student_required], name='dispatch')
class ExamListView(views.ListView):
    model = Exam
    ordering = ('name',)
    context_object_name = 'exams'
    template_name = 'exam/exam_list.html'

    def get_queryset(self):
        student = self.request.user.student
        student_interests = student.interests.values_list('pk', flat=True)
        taken_exams = student.exams.values_list('pk', flat=True)
        queryset = Exam.objects.filter(subject__in=student_interests) \
            .exclude(pk__in=taken_exams) \
            .annotate(questions_count=Count('question')) \
            .filter(questions_count__gt=0)
        return queryset

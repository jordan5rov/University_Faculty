from django.views import generic as views


class StudentExamView(views.TemplateView):
    template_name = 'exam/student_exam.html'

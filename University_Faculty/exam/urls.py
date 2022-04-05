from django.urls import path

from University_Faculty.exam.views.student import StudentExamView

urlpatterns = (
    path('student', StudentExamView.as_view(), name='student exam'),
)

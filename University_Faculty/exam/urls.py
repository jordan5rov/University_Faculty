from django.urls import path

from University_Faculty.exam.views.student import ExamListView, StudentInterestsView

urlpatterns = (
    path('student', ExamListView.as_view(), name='students exam'),
    path('student/interests', StudentInterestsView.as_view(), name='students interests'),
)

from django.urls import path

from University_Faculty.classroom.views.authentication import RegisterView, StudentRegisterView, TeacherRegisterView

urlpatterns = (
    path('register', RegisterView.as_view(), name='register'),
    path('register/student', StudentRegisterView.as_view(), name='register student'),
    path('register/register', TeacherRegisterView.as_view(), name='register teacher'),
)
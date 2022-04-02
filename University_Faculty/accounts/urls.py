from django.urls import path
from University_Faculty.accounts.views.generic import UserLogoutView, RegisterView
from University_Faculty.accounts.views.students import StudentRegisterView, StudentLoginView
from University_Faculty.accounts.views.teachers import TeacherRegisterView

urlpatterns = (
    path('register', RegisterView.as_view(), name='register'),
    path('register/student', StudentRegisterView.as_view(), name='register student'),
    path('login/student', StudentLoginView.as_view(), name='login student'),
    path('register/teacher', TeacherRegisterView.as_view(), name='register teacher'),
    path('logout', UserLogoutView.as_view(), name='logout'),

)



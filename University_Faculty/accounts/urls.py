from django.urls import path
from University_Faculty.accounts.views.generic import UserLogoutView, UserRegisterView, UserLoginView
from University_Faculty.accounts.views.students import StudentRegisterView
from University_Faculty.accounts.views.teachers import TeacherRegisterView

urlpatterns = (
    path('register', UserRegisterView.as_view(), name='register'),
    path('register/student', StudentRegisterView.as_view(), name='register student'),
    path('register/teacher', TeacherRegisterView.as_view(), name='register teacher'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
)

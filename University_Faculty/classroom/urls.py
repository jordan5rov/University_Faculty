from django.urls import path

from University_Faculty.classroom.views.authentication import RegisterView, StudentRegisterView, TeacherRegisterView, \
    LoginView, LogoutView
from University_Faculty.classroom.views.teachers import QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView, \
    QuizResultsView

urlpatterns = (
    path('register', RegisterView.as_view(), name='register'),
    path('register/student', StudentRegisterView.as_view(), name='register student'),
    path('register/register', TeacherRegisterView.as_view(), name='register teacher'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('quizzes', QuizListView.as_view(), name='quizzes'),
    path('quiz/create', QuizCreateView.as_view(), name='create quiz'),
    path('quiz/update/<int:pk>/', QuizUpdateView.as_view(), name='update quiz'),
    path('quiz/delete/<int:pk>/', QuizDeleteView.as_view(), name='delete quiz'),
    path('quiz/<int:pk>/result', QuizResultsView.as_view(), name='result quiz'),
)

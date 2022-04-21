from django.urls import path

from University_Faculty.classroom.views.authentication import RegisterView, StudentRegisterView, TeacherRegisterView, \
    LoginView, LogoutView
from University_Faculty.classroom.views.questions import create_question_view, edit_question_view, QuestionDeleteView
from University_Faculty.classroom.views.quizzes import QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView, \
    QuizResultsView
from University_Faculty.classroom.views.students import StudentInterestView, take_quiz_view, quiz_data_view, \
    quiz_save_view, QuizTakenListView

urlpatterns = (
    path('register', RegisterView.as_view(), name='register'),
    path('register/student', StudentRegisterView.as_view(), name='register student'),
    path('register/register', TeacherRegisterView.as_view(), name='register teacher'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('quizzes', QuizListView.as_view(), name='quizzes'),
    path('quizzes/taken/', QuizTakenListView.as_view(), name='taken quizzes'),
    path('quiz/create', QuizCreateView.as_view(), name='create quiz'),
    path('quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='update quiz'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='delete quiz'),
    path('quiz/<int:pk>/result/', QuizResultsView.as_view(), name='result quiz'),

    path('quiz/<int:pk>/question/create/', create_question_view, name='create question'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/update/', edit_question_view, name='update question'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', QuestionDeleteView.as_view(), name='delete question'),

    path('student/interests/', StudentInterestView.as_view(), name='interests student'),
    path('quiz/<int:pk>/', take_quiz_view, name='take quiz'),
    path('quiz/<int:pk>/data/', quiz_data_view, name='data quiz'),
    path('quiz/<int:pk>/save/', quiz_save_view, name='save quiz'),
)

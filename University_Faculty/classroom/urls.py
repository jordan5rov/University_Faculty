from django.urls import path

from .views import authentication, questions, students, teachers
from .views.teachers import CreateSubjectView

urlpatterns = (
    path('register', authentication.RegisterView.as_view(), name='register'),
    path('register/student', authentication.StudentRegisterView.as_view(), name='register student'),
    path('register/register', authentication.TeacherRegisterView.as_view(), name='register teacher'),
    path('login', authentication.LoginView.as_view(), name='login'),
    path('logout', authentication.LogoutView.as_view(), name='logout'),

    path('student/quizzes', students.QuizListView.as_view(), name='student quizzes'),
    path('quizzes/taken/', students.QuizTakenListView.as_view(), name='taken quizzes'),
    path('student/interests/', students.StudentInterestView.as_view(), name='interests student'),
    path('quiz/<int:pk>/', students.take_quiz_view, name='take quiz'),
    path('quiz/<int:pk>/data/', students.quiz_data_view, name='data quiz'),
    path('quiz/<int:pk>/save/', students.quiz_save_view, name='save quiz'),

    path('teacher/quizzes', teachers.QuizListView.as_view(), name='teacher quizzes'),
    path('quiz/create', teachers.QuizCreateView.as_view(), name='create quiz'),
    path('quiz/<int:pk>/update/', teachers.QuizUpdateView.as_view(), name='update quiz'),
    path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='delete quiz'),
    path('quiz/<int:pk>/result/', teachers.QuizResultsView.as_view(), name='result quiz'),
    path('subject/create/', CreateSubjectView.as_view(), name='create subject'),

    path('quiz/<int:pk>/question/create/', questions.create_question_view, name='create question'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/update/', questions.edit_question_view, name='update question'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', questions.QuestionDeleteView.as_view(),
         name='delete question'),


)

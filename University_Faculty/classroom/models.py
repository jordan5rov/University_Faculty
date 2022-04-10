from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.html import escape, mark_safe
from University_Faculty.common.constants import *
from University_Faculty.classroom.managers import UniversityUserManager


class UniversityUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USER_TYPES = [(x, x) for x in [STUDENT, TEACHER, ADMIN]]
    type = models.CharField(choices=USER_TYPES, max_length=max(len(x) for (x, _) in USER_TYPES), default=STUDENT)
    objects = UniversityUserManager()


class Subject(models.Model):
    name = models.CharField(max_length=SUBJECT_NAME_MAX_LENGTH, unique=True)
    color = models.CharField(max_length=COLOR_MAX_LENGTH, default=COLOR_DEFAULT)

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(UniversityUser, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=QUIZ_NAME_MAX_LENGTH, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(UniversityUser, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(UniversityUser, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, related_name='created_quizzes')
    specialization = models.ManyToManyField(Subject, related_name='teachers_specialization')

    def __str__(self):
        return self.user.username


class Question(models.Model):
    OPTIONS = [(x, x) for x in [OPTION_1, OPTION_2, OPTION_3, OPTION_4]]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=QUESTION_MAX_LENGTH)
    option_1 = models.CharField(max_length=OPTIONS_MAX_LENGTH)
    option_2 = models.CharField(max_length=OPTIONS_MAX_LENGTH)
    option_3 = models.CharField(max_length=OPTIONS_MAX_LENGTH)
    option_4 = models.CharField(max_length=OPTIONS_MAX_LENGTH)
    correct_option = models.CharField(max_length=max(len(x) for x, _ in OPTIONS), choices=OPTIONS)

    def __str__(self):
        return self.question


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='+')

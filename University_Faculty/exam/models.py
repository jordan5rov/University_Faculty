from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import escape, mark_safe

#
# UserModel = get_user_model()
from University_Faculty import accounts


class Subject(models.Model):
    NAME_MAX_LENGTH = 50
    COLOR_MAX_LENGTH = 7
    COLOR_DEFAULT = '#007bff'
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    color = models.CharField(max_length=COLOR_MAX_LENGTH, default=COLOR_DEFAULT)

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = f'<span class="badge badge-primary" style="background-color: {color}">{name}</span>'
        return mark_safe(html)


class Exam(models.Model):
    NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_MAX_LENGTH = 200
    OPTION_MAX_LENGTH = 50

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.CharField(max_length=QUESTION_MAX_LENGTH)
    option_1 = models.CharField(max_length=OPTION_MAX_LENGTH)
    option_2 = models.CharField(max_length=OPTION_MAX_LENGTH)
    option_3 = models.CharField(max_length=OPTION_MAX_LENGTH)
    option_4 = models.CharField(max_length=OPTION_MAX_LENGTH)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    correct_option = models.CharField(max_length=QUESTION_MAX_LENGTH, choices=cat)

    def __str__(self):
        return self.question


class Result(models.Model):
    student = models.ForeignKey("accounts.Student", on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

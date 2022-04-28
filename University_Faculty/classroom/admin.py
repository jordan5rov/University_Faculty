from django.contrib import admin
from .models import *


@admin.register(UniversityUser)
class UniversityUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
    list_display_links = ('id', 'username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    list_per_page = 50
    ordering = ('username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture')
    list_display_links = ('user', 'picture')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 50
    ordering = ('user',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture')
    list_display_links = ('user', 'picture')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 50
    ordering = ('user',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'time', 'required_score_to_pass', 'max_score')
    list_display_links = ('name', 'subject', 'time', 'required_score_to_pass', 'max_score')
    list_filter = ('name', 'subject', 'time', 'required_score_to_pass', 'max_score')
    search_fields = ('name', 'subject', 'time', 'required_score_to_pass', 'max_score')
    list_per_page = 50
    ordering = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'quiz',)
    list_display_links = ('question', 'quiz',)
    list_filter = ('question', 'quiz',)
    search_fields = ('question', 'quiz',)
    list_per_page = 50
    ordering = ('question',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_display_links = ('name', 'color')
    list_filter = ('name', 'color')
    search_fields = ('name', 'color')
    list_per_page = 50
    ordering = ('name',)

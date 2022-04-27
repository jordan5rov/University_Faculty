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
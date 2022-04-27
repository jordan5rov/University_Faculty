from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'published_on')
    list_filter = ('published_on',)
    search_fields = ('title',)
    date_hierarchy = 'published_on'
    ordering = ('published_on',)
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image', 'description')
    list_filter = ('date',)
    search_fields = ('title',)
    date_hierarchy = 'date'
    ordering = ('date',)

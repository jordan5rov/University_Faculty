from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'publish')
    # list_filter = ('publish', 'author')
    # search_fields = ('title', 'body')
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('publish',)
    pass

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    # list_display = ('title', 'event_date', 'event_time', 'location')
    # list_filter = ('event_date', 'location')
    # search_fields = ('title', 'location')
    # date_hierarchy = 'event_date'
    # ordering = ('event_date',)
    pass
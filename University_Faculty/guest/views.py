from django.shortcuts import render
from django.views import generic as views


class Index(views.TemplateView):
    template_name = 'base.html'

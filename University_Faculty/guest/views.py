from django.shortcuts import render
from django.views import generic as views


class Index(views.TemplateView):
    template_name = 'home.html'


class About(views.TemplateView):
    template_name = 'about.html'


class Contact(views.TemplateView):
    template_name = 'contact.html'


class Post(views.TemplateView):
    template_name = 'post.html'

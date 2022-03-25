from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.web.models import News, Event


class HomeView(views.ListView):
    model = News
    template_name = 'web/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context


class NewsCreate(views.CreateView):
    model = News
    template_name = 'web/create_news.html'
    fields = ('title', 'image', 'description')
    success_url = reverse_lazy('home')
    # news = News.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewsDetails(views.DetailView):
    model = News
    template_name = 'web/news_details.html'
    context_object_name = 'news'


class NewsEdit(views.UpdateView):
    template_name = 'web/news_edit.html'


class NewsDelete(views.DeleteView):
    template_name = 'web/news_delete.html'


class EventDetails(views.DetailView):
    template_name = 'web/event_details.html'


class EventEdit(views.UpdateView):
    template_name = 'web/event_edit.html'


class EventDelete(views.DeleteView):
    template_name = 'web/event_delete.html'

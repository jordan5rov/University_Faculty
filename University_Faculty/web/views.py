from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.web.forms import CreateNewsForm
from University_Faculty.web.models import News, Event


class HomeView(views.ListView):
    model = News
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = list(News.objects.all())
        start_index = len(news) - 4
        last_four_news = news[start_index: len(news)]
        last_four_news.reverse()
        context['news'] = last_four_news
        context['events'] = Event.objects.all()
        return context


class NewsCreate(views.CreateView):
    model = News
    template_name = 'web/news_create.html'
    success_url = reverse_lazy('home')
    form_class = CreateNewsForm

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


class NewsDetails(views.DetailView):
    model = News
    template_name = 'web/news_details.html'
    context_object_name = 'news'


class NewsEdit(views.UpdateView):
    template_name = 'web/news_edit.html'


class NewsDelete(views.DeleteView):
    template_name = 'web/news_delete.html'


class NewsSeeMore(views.ListView):
    template_name = 'web/news_see_more.html'
    model = News
    paginate_by = 10
    context_object_name = 'news'


class EventDetails(views.DetailView):
    template_name = 'web/event_details.html'


class EventEdit(views.UpdateView):
    template_name = 'web/event_edit.html'


class EventDelete(views.DeleteView):
    template_name = 'web/event_delete.html'

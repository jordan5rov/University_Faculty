from django.urls import reverse_lazy
from django.views import generic as views
from University_Faculty.web.models import News, Event


class HomeView(views.ListView):
    model = News
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = list(News.objects.all())
        news.reverse()
        context['news'] = news[0:4]
        context['events'] = Event.objects.all()
        return context

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from University_Faculty.web.models import News, Event


class HomeView(views.ListView):
    model = News
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-published_on')[:3]

        context['events'] = Event.objects.all().order_by('date')[0:3]

        return context


def handler404(request, exception):
    return render(request, 'web/404_handler.html')

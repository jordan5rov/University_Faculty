from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.web.forms import CreateNewsForm
from University_Faculty.web.models import News


class NewsCreate(views.CreateView):
    model = News
    template_name = 'web/news_create.html'
    success_url = reverse_lazy('home')
    form_class = CreateNewsForm

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


class NewsDetailsView(views.DetailView):
    model = News
    template_name = 'web/news_details.html'
    context_object_name = 'news'


class NewsEditView(views.UpdateView):
    template_name = 'web/news_edit.html'


class NewsDeleteView(views.DeleteView):
    template_name = 'web/news_delete.html'


class NewsSeeMoreView(views.ListView):
    template_name = 'web/news_see_more.html'
    model = News
    paginate_by = 10
    context_object_name = 'news'

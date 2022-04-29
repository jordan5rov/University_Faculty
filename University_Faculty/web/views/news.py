from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from University_Faculty.common.decorators import teacher_required
from University_Faculty.web.forms import CreateNewsForm, DeleteNewsForm, EditNewsForm
from University_Faculty.web.models import News


@method_decorator([login_required, teacher_required], name='dispatch')
class NewsCreate(views.CreateView):
    model = News
    template_name = 'web/news_create.html'
    success_url = reverse_lazy('home')
    form_class = CreateNewsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewsDetailsView(views.DetailView):
    model = News
    template_name = 'web/news.html'
    context_object_name = 'news'


@method_decorator([login_required, teacher_required], name='dispatch')
class NewsEditView(views.UpdateView):
    template_name = 'web/news_edit.html'
    model = News
    form_class = EditNewsForm
    success_url = reverse_lazy('see more news')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NewsSeeMoreView(views.ListView):
    template_name = 'web/news_see_more.html'
    model = News
    paginate_by = 10
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all().order_by('-published_on')


@method_decorator([login_required, teacher_required], name='dispatch')
class NewsDeleteView(views.DeleteView):
    model = News
    template_name = 'web/news_delete.html'
    success_url = reverse_lazy('see more news')
    form_class = DeleteNewsForm

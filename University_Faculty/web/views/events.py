from django.urls import reverse_lazy
from django.views import generic as views

from University_Faculty.web.forms import CreateEventForm, EditEventForm, DeleteEventForm
from University_Faculty.web.models import Event


class EventCreateView(views.CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'web/event_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventSeeMoreView(views.ListView):
    template_name = 'web/event_see_more.html'
    model = Event
    paginate_by = 10
    context_object_name = 'events'


class EventDetailsView(views.DetailView):
    model = Event
    template_name = 'web/event.html'
    context_object_name = 'event'


class EventEditView(views.UpdateView):
    template_name = 'web/event_edit.html'
    model = Event
    form_class = EditEventForm
    success_url = reverse_lazy('see more event')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDeleteView(views.DeleteView):
    model = Event
    template_name = 'web/event_delete.html'
    success_url = reverse_lazy('see more news')
    form_class = DeleteEventForm

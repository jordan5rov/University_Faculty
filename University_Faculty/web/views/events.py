from django.views import generic as views


class EventDetailsView(views.DetailView):
    template_name = 'web/event_details.html'


class EventEditView(views.UpdateView):
    template_name = 'web/event_edit.html'


class EventDeleteView(views.DeleteView):
    template_name = 'web/event_delete.html'

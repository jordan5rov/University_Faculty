from django.urls import path

from University_Faculty.web.views.events import EventDetailsView, EventEditView, EventDeleteView
from University_Faculty.web.views.generic import HomeView
from University_Faculty.web.views.news import NewsCreate, NewsDetailsView, NewsEditView, NewsDeleteView, NewsSeeMoreView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('news/create', NewsCreate.as_view(), name='create news'),
    path('news/', NewsDetailsView.as_view(), name='news'),
    path('news/edit', NewsEditView.as_view(), name='edit news'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='delete news'),
    path('news/see-more', NewsSeeMoreView.as_view(), name='see more news'),

    path('event/details', EventDetailsView.as_view(), name='details event'),
    path('event/edit', EventEditView.as_view(), name='edit event'),
    path('event/delete', EventDeleteView.as_view(), name='delete event'),

)

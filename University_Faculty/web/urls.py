from django.urls import path

from University_Faculty.web.views.events import EventDetailsView, EventEditView, EventDeleteView, EventCreateView, \
    EventSeeMoreView
from University_Faculty.web.views.generic import HomeView
from University_Faculty.web.views.news import NewsCreate, NewsDetailsView, NewsEditView, NewsDeleteView, NewsSeeMoreView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('news/create/', NewsCreate.as_view(), name='create news'),
    path('news/edit/<int:pk>/', NewsEditView.as_view(), name='edit news'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='delete news'),
    path('news/<int:pk>/', NewsDetailsView.as_view(), name='read news'),
    path('news/see-more/', NewsSeeMoreView.as_view(), name='see more news'),

    path('event/create/', EventCreateView.as_view(), name='create event'),
    path('event/<int:pk>/', EventDetailsView.as_view(), name='view event'),
    path('event/edit/<int:pk>/', EventEditView.as_view(), name='edit event'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='delete event'),
    path('event/see-more/', EventSeeMoreView.as_view(), name='see more event'),

)

from django.urls import path

from University_Faculty.web.views.generic import HomeView
from University_Faculty.web.views import events, news

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('news/create/', news.NewsCreate.as_view(), name='create news'),
    path('news/edit/<int:pk>/', news.NewsEditView.as_view(), name='edit news'),
    path('news/delete/<int:pk>/', news.NewsDeleteView.as_view(), name='delete news'),
    path('news/<int:pk>/', news.NewsDetailsView.as_view(), name='read news'),
    path('news/see-more/', news.NewsSeeMoreView.as_view(), name='see more news'),

    path('event/create/', events.EventCreateView.as_view(), name='create event'),
    path('event/<int:pk>/', events.EventDetailsView.as_view(), name='view event'),
    path('event/edit/<int:pk>/', events.EventEditView.as_view(), name='edit event'),
    path('event/delete/<int:pk>/', events.EventDeleteView.as_view(), name='delete event'),
    path('event/see-more/', events.EventSeeMoreView.as_view(), name='see more event'),

)

from django.urls import path

from University_Faculty.web.views import HomeView, NewsDetails, NewsEdit, EventDetails, EventEdit, NewsDelete, \
    EventDelete, NewsCreate, NewsSeeMore

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('news-create/', NewsCreate.as_view(), name='create news'),
    path('news-details/', NewsDetails.as_view(), name='details news'),
    path('news-edit/', NewsEdit.as_view(), name='edit news'),
    path('news-delete/', NewsDelete.as_view(), name='delete news'),
    path('news-see-more/', NewsSeeMore.as_view(), name='see more news'),

    path('event-details/', EventDetails.as_view(), name='details event'),
    path('event-edit', EventEdit.as_view(), name='edit event'),
    path('event-delete', EventDelete.as_view(), name='delete event'),

)

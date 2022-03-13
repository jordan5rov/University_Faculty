from django.urls import path

from University_Faculty.guest.views import Index, About, Post, Contact

urlpatterns = (
    path('', Index.as_view(), name='index'),
)
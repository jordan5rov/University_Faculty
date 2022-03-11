from django.urls import path

from University_Faculty.guest.views import Index

urlpatterns = (
    path('', Index.as_view(), name='index'),
)

from django.urls import path

from University_Faculty.web.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)

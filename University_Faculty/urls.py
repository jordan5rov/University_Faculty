"""
 ctrl + k, ctrl + enter -> commit
 ctrl + shift + k, ctrl + enter -> push
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('University_Faculty.web.urls'))
)


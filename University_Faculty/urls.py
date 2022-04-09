from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

"""
 ctrl + k, ctrl + enter -> commit
 ctrl + shift + k, ctrl + enter -> push
"""

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('University_Faculty.web.urls')),
    path('', include('University_Faculty.classroom.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

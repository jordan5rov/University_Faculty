from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('University_Faculty.web.urls')),
    path('', include('University_Faculty.classroom.urls')),
]
handler404 = 'University_Faculty.web.views.generic.handler404'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

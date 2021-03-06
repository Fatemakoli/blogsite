from django.conf import settings
from App import views
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', travel, name='travel'),
    path('<int:id>/', blog_travel, name='btravel'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
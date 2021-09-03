from App import views
from .views import *
from django.urls import path


urlpatterns = [
    path('', fashion, name='fashion'),
    path('<int:id>/', blog_fashion, name='bfashion'),
]
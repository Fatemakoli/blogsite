from .views import *
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
     path('contact/', contact, name='contact'), 
     path('email/', email), 

]
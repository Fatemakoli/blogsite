from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def travel(request):
    travels = Travel.objects.all() 
    context = {
    "object_list" : travels,
    }    
    return render(request, 'travel.html', context)



def blog_travel(request, id):
    travelpost = get_object_or_404(Travel, pk=id) 
    context = {
    "single_post" : travelpost,
        }
    return render(request, 'tblog.html', context )


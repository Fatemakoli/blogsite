from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def beauty(request):
   queryset = Beauty.objects.all()
   context = {
        "object_list": queryset,
     }
   return render(request, 'beauty.html', context)


def blog(request, id):
      
      queryset1 = get_object_or_404(Beauty, pk=id)
      
      context = {
         "single_post": queryset1,
      }
      return render(request, 'bblog.html', context )

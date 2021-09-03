from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def fashion(request):
    fashion = Fashion.objects.all() 
    context = {
        "object_list" : fashion,
    }
    return render(request, 'fashion.html', context)


def blog_fashion(request, id):
      queryset1 = get_object_or_404(Fashion, pk=id) 
      context = {
      "single_post": queryset1,
      }
      return render(request, 'fblog.html', context )

from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, 'index.html', context)
    

def contact(request):
    if request.method == "POST":
        var1 = request.POST.get("name")
        var2 = request.POST.get("email")
        var3 = request.POST.get("subject")
        var4= request.POST.get("phone")
        var5 = request.POST.get("message")

        message_body = var1+ '\n' + var2 + '\n' +var3 + '\n' + var4 + "\n" + var5
        send_mail(
            'Contact Form [Beaty Blog]',
            message_body,
            settings.EMAIL_FROM,
            ['raihan.tusher@yahoo.com'],
            fail_silently=False,
        )
        
    return render(request, 'contact.html')


def email(request):
   send_mail(
      'Subject here',
      'Here is the message.',
      settings.EMAIL_FROM,
      ['raihan.tusher@yahoo.com'],
      fail_silently=False,
   )
   return HttpResponse( " mail sent!")
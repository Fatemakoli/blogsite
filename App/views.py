from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def beauty(request):
    return render(request, 'beauty.html')

def fashion(request):
    return render(request, 'fashion.html')

def travel(request):
    return render(request, 'travel.html')

def contact(request):
    return render(request, 'contact.html')
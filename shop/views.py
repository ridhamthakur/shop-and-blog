from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("at contact us")

def tracker(request):
    return HttpResponse("at tracker")

def productView(request):
    return HttpResponse("at product Views")

def search(request):
    return HttpResponse("at search")

def checkout(request):
    return HttpResponse("at checkout")
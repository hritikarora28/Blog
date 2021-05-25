from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('we are in home')
def contact(request):
    return render(request,'home/contact.html')
    # return HttpResponse('we are in contact')
def about(request):
     return render(request,'home/about.html')
    # return HttpResponse('we are in about')

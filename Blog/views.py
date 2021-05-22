from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(index):
    return HttpResponse('we are in home')
def blog(index):
    return HttpResponse('we are in blog')

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(index):
    return HttpResponse('we are in request')
def contact(index):
    return HttpResponse('we are in request')
def about(index):
    return HttpResponse('we are in request')

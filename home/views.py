from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('we are in home')
def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        print(f'{name},{email},{phone},{msg}')
        contact = Contact(name=name, email=email,phone=phone, content=msg)
        contact.save()
    return render(request,'home/contact.html')
    
def about(request):
     return render(request,'home/about.html')
    # return HttpResponse('we are in about')

from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from blog.models import Post

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
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            messages.success(request,"your call was sucessful")
            contact = Contact(name=name, email=email,phone=phone, content=msg)
            contact.save()
    return render(request,'home/contact.html')
    
def about(request):
     return render(request,'home/about.html')
    # return HttpResponse('we are in about')
def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)

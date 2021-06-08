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
    if len(query) >78:
        allPosts=[]
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAutor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAutor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")    
    params={'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)

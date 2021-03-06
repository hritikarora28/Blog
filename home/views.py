from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
def handleSignup(request):
    if request.method =='POST':
        #Get The post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #checks for erroneous input
        if len(username)>15:
            messages.error(request,"Username must be less the 10 characters")
            return redirect('/')
        if  username.isalpha():
            messages.error(request,"Username must be Alpha Numeric")
            return redirect('/')
        if pass1!=pass2:
            messages.error(request,"Passwords don't match please try again")
            return redirect('/')

        #create user
        myuser = User.objects.create_user(username,email,pass1)
        myuser_fname = fname
        myuser_lname = lname
        myuser.save()
        messages.success(request,"Your Acoount Has Been Sucessfully Created")
        return redirect('/')
    else:
        return HttpResponse("404-Not Allowed")
def handleLogin(request):
    if request.method =='POST':
        #Get The post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username= loginusername,password= loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome back {loginusername}.Hope you are doing Well ")
            return redirect("/")
        else:
            messages.error(request,"Either password or user name is worng")
            return redirect("/")
    return HttpResponse('Go and login,donont try to be over smart')
def handleLogout(request):
    logout(request)
    messages.success(request,"You are sucessfully logout")
    return redirect("/")
    
    
    
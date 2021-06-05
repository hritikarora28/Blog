from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    
    return render(request,'blog/blogHome.html',context)
    # return HttpResponse('this is bloghome we will keep all the blogpost here')


def blogPost(request,slug):
     return render(request,'blog/blogPost.html')
    # return HttpResponse(f"this is blogPost {slug}")
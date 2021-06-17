from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    # api to post comment
    path('postComment',views.postComment,name='postComment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    # api to post comment
     
    
]
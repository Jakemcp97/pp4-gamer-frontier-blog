from . import views
from django.urls import path, include
from .views import *


app_name = 'blog'


urlpatterns = [
    # home
    path('', views.postslist.as_view(), name='home'),
    # add post
    path('blog_post/', views.blog_post, name='blog_post'),
    # success for blog post
    path('success/', views.success, name='success'),
    # posts
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
]

from . import views
from django.urls import path, include
from .views import *


urlpatterns = [
    # home
    path('', views.postslist.as_view(), name='home'),
    # add post
    path('blog_post/', views.PostCreateView.as_view(), name='blog_post'),
    # edit post 
    path('blog_post/<int:pk>/', views.Editpost().as_view(), name='edit_post'),
    # delete post 
    path('blog_post/<int:pk>/delete/', views.Deletepost().as_view(), name='delete_post'),
    # posts/comments
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
    # likes
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

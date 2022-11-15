from . import views
from django.urls import path, include
from .views import *


urlpatterns = [
    # home
    path('', views.postslist.as_view(), name='home'),
    # add post
    path('blog_post/', views.PostCreateView.as_view(), name='blog_post'),
    # posts/comments
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
    # edit post
    path('<slug:slug>/edit/', views.Editpost.as_view(), name='edit_post'),
    # delete post
    path('<int:pk>/delete/', views.Deletepost.as_view(), name='delete_post'),
    # likes
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

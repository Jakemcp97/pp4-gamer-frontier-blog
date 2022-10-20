from . import views
from django.urls import path, include
from .views import *
from .views import create_post


urlpatterns = [
    # home
    path('', views.postslist.as_view(), name='home'),
    # posts
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
    # add post
    path('add/', views.create_post, name='create_post'),
]

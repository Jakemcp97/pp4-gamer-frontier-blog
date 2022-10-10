from . import views
from django.urls import path, include
from .views import *


urlpatterns = [
    # home
    path('', views.postslist.as_view(), name='home'),
    # posts
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail')
]

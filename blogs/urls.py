from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "blog"
urlpatterns = [
    path('blog_all/', views.blog_all, name='blog_all'),
    path('blog_single/<int:id>', views.blog_single, name='blog_single'),
]
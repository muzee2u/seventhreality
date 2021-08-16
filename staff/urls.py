from django.contrib import admin
from django.urls import path
from . import views

# app_name = "RD_Project"
app_name = 'staff'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:id>', views.staff_detail, name="staff_detail")
]
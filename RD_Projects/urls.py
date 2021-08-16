from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

# app_name = "RD_Project"
app_name = 'RD_Project'
urlpatterns = [
    path('Project_Domains/', views.project_domains, name='Project_domains'),
    path('projects_all', views.projects_all, name='projects_all'),
    path('projects_single/<str:id>', views.project_single, name='projects_single'),
    path('services/', views.services, name="services"),
    path('services/<str:id>', views.service_single, name="services_single"),
    path('get_project_detail/', views.get_project_detail, name="get_project_detail"),
    path('get_service_detail/', views.get_service_detail, name="get_service_detail")
]

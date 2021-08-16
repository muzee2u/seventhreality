from django.urls import path, include
from . import views


app_name = "publication"
urlpatterns = [
    path('publications_all/', views.publications_all, name='publications_all'),
]
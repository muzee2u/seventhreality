from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/Staff_Pics')
    profile = RichTextField(default="")

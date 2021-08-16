from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    siteLink = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/blogs_img', null=True, blank=True)
    content = RichTextField(default="")

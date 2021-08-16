from datetime import datetime
from django.db import models


# Create your models here.
class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    publishDate = models.DateField(default=datetime.now)
    siteLink = models.CharField(max_length=300)

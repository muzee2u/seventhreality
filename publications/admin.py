from django.contrib import admin
from .models import *


# Register your models here.
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('publishDate', 'author', 'title')


admin.site.register(ResearchPaper, ResearchPaperAdmin)

from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_all(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog-all.html', {'blogs': blogs})


def blog_single(request, id):
    blog = Blog.objects.filter(id=id)
    return render(request, 'blogs/blog-single.html', {'blog': blog})

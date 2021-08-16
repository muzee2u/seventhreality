from django.shortcuts import render


# Create your views here.
def publications_all(request):
    return render(request, 'publications/publications-all.html')

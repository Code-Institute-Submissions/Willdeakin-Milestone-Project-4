from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

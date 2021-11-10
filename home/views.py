from django.shortcuts import render
from store.models import Products
from blog.models import Post


# Create your views here.

def index(request):
    """ A view to return the index page """
    products = Products.objects.all()
    posts = Post.objects.all()
    context = {
        'products': products,
        'posts': posts,
    }
    return render(request, 'home/index.html', context)

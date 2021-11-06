from django.shortcuts import render
from django.http import HttpResponse
from store.models import Products


# Create your views here.

def index(request):
    """ A view to return the index page """
    products = Products.objects.all()
    home_nums = [5, 10]
    context = {
        'products': products,
        'home_nums': home_nums,
    }
    return render(request, 'home/index.html', context)

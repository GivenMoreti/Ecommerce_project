from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from.forms import SearchForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/index.html",context)


# implement search products

def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__icontains=query)

    context = {
        'form':form,"results":results
    }    
    return render(request,"products/search_results.html",context)

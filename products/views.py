from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product, UserProfile, CartItem, Cart, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SearchForm

# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products/index.html", context)


# implement search products

def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__icontains=query)

    context = {
        'form': form, "results": results
    }
    return render(request, "products/search_results.html", context)


def cart(request, id):
    carts = CartItem.objects.filter(id=id)

    context = {"carts": carts}
    return render(request, "products/cart.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)

        except:
            # messages.error(request,'username or password incorrect')
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password incorrect')

    return render(request, 'products/login.html')


def logout_user(request):
    logout(request)
    return redirect("home")

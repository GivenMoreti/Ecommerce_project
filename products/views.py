from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import About, Product, UserProfile, CartItem, Cart, Category, SaleItem, Sell
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SearchForm, SellNowForm, UserProfileForm
from .forms import RegistrationForm
# Create your views here.


def home(request):
    # display all products that arent sold.
    products = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        'products': products,
        "categories": categories,
    }
    return render(request, "products/index.html", context)

# when you click on an item it must open the details page of that item.


def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products/detail.html", context)


# implement search products


def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        # can search by Product,Category,user(seller),description
        results = Product.objects.filter(
            name__icontains=query) or Category.objects.filter(
            name__icontains=query)

    context = {
        'form': form, "results": results
    }
    return render(request, "products/search_results.html", context)


def cart(request):
    cart_items = CartItem.objects.all()
    context = {"cart_items": cart_items}
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


# discounted items
def sale(request):
    sale_items = SaleItem.objects.all()

    context = {"sale_items": sale_items}
    return render(request, "products/sale.html", context)


@login_required
# def sell(request):
#     sold_items= Sell.objects.all()
#     context = {"sold_items":sold_items}
#     return render(request,"products/sell_now.html",context)
def sell(request):
    if request.method == 'POST':
        form = SellNowForm(request.POST)
        if form.is_valid():
            form.save()
            # Replace 'success' with the appropriate URL name for the success page
            return redirect('home')
    else:
        form = SellNowForm()
    return render(request, 'products/sell_now.html', {'form': form})


def seller_profile(request):
    if request.method == 'POST':
        form_two = UserProfileForm(request.POST)
        if form_two.is_valid():
            form_two.save()
            # Replace 'success' with the appropriate URL name for the success page
            return redirect('home')
    else:
        form_two = UserProfileForm()
    return render(request, 'products/sell_now.html', {'form_two': form_two})

# register a user to a database


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'products/register.html', {'form': form})


# about page
def about(request):
    about = About.objects.all()
    
    return render(request,"products/about.html",{"about":about})
from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/index.html",context)


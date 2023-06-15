from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("cart/",views.cart,name="cart"),
    path("sale/",views.sale,name="sale"),

]

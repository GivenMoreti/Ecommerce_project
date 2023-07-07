from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm
# app_name = "product"

urlpatterns = [
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),

    path("login/",auth_views.LoginView.as_view(template_name="products/login.html",authentication_form=LoginForm),name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("cart/",views.cart,name="cart"),
    path("sale/",views.sale,name="sale"),
    # path('update_card/<int:pk>/', views.update_card, name='update_cd'),
    path('sell_now/',views.sell,name="sell_now"),
    path('register/', views.register_user, name='register'),
    path("details/<int:pk>/",views.details,name="details"),
    path("about/",views.about,name="about")



]

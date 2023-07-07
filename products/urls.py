from django.contrib import admin
from django.urls import path
from . import views


# app_name = "product"

urlpatterns = [
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("cart/",views.cart,name="cart"),
    path("sale/",views.sale,name="sale"),
    # path('update_card/<int:pk>/', views.update_card, name='update_cd'),
    path('sell_now/',views.sell,name="sell_now"),
    path('register/', views.register_user, name='register'),
    path("details/<int:pk>/",views.details,name="details"),



]

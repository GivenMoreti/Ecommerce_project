from django.contrib import admin
# Register your models here.
from .models import Category,Product,UserProfile,Cart,Order,CartItem,Address,Payment

class CategoryModel(admin.ModelAdmin):
    list_display = ("name",)

class ProductModel(admin.ModelAdmin):
    list_display = ("name","description","price","quantity")

class CartModel(admin.ModelAdmin):
    list_display = ("user",)

class CartItemModel(admin.ModelAdmin):
    list_display = ("cart","product","quantity")

class AddressModel(admin.ModelAdmin):
    list_display = ("user","street","city","province")

class UserProfileModel(admin.ModelAdmin):
    list_display = ("user","products")


admin.site.register(Category,CategoryModel)
admin.site.register(Product,ProductModel)
admin.site.register(UserProfile)
admin.site.register(Cart,CartModel)
admin.site.register(Order)
admin.site.register(CartItem,CartItemModel)
admin.site.register(Payment)
admin.site.register(Address,AddressModel)
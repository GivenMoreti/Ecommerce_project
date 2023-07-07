from django.contrib import admin
# Register your models here.
from .models import Category, Product, UserProfile, Cart, Order, CartItem, Address, Payment, SaleItem, Sell, Delivery, About


class CategoryModel(admin.ModelAdmin):
    list_display = ("name",)


class ProductModel(admin.ModelAdmin):
    list_display = ("name", "description", "price", "quantity", "sold_by")


class CartModel(admin.ModelAdmin):
    list_display = ("user",)


class CartItemModel(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")


class AddressModel(admin.ModelAdmin):
    list_display = ("user", "street", "city", "province")


class UserProfileModel(admin.ModelAdmin):
    list_display = ("user",)


class SaleItemModel(admin.ModelAdmin):
    list_display = ("products", "title", "code")


class SellModel(admin.ModelAdmin):
    list_display = ("products", "category", "user", "address", "date_added")


class DeliveryModel(admin.ModelAdmin):
    list_display = ("order", "order_date", "delivery_date",)


admin.site.register(Delivery, DeliveryModel)
admin.site.register(Category, CategoryModel)
admin.site.register(Product, ProductModel)
admin.site.register(UserProfile, UserProfileModel)
admin.site.register(Cart, CartModel)
admin.site.register(Order)
admin.site.register(CartItem, CartItemModel)
admin.site.register(Payment)
admin.site.register(Address, AddressModel)
admin.site.register(SaleItem, SaleItemModel)
admin.site.register(Sell, SellModel)
admin.site.register(About)



from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=8000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # include timesence in index.html
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
        # NOT NULL constraint failed: products_userprofile.products_id
    # products = models.ManyToManyField(Product,related_name='products')
    
    def __str__(self):
        return f"{self.user.username} {self.products.name}" 

    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"items added to cart: {self.product.name}"


PROVINCES = (
    ("Limpopo", "Lim"),
    ("Free state", "Fs"),
    ("Gauteng", "Gau")
)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100, choices=PROVINCES)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.city} {self.postal_code}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order Number: {self.pk}"


PAYMENT_METHODS = (
    ("EFT", "EFT"),
    ("CASH", "CASH")
)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_menthod = models.CharField(choices=PAYMENT_METHODS, max_length=30)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for Order Number{self.order.pk}"


class SaleItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # 10 % discount
    code = models.CharField(max_length=10)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Discount applied on these items {self.products}"

    class Meta:
        ordering = ['-products']


class Sell(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is selling{self.products} with {self.category}"
    
    class Meta:
        ordering = ['date_added']
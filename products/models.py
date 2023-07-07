from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    # validate if category already exists
    def clean(self):
        existing_category = Category.objects.filter(
            name=self.name).exclude(pk=self.pk)
        if existing_category.exists():
            raise ValidationError("Category with this name already exists.")


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=8000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # include timesence in index.html
    is_sold = models.BooleanField(default=False,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    sold_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    # discount = models.PositiveIntegerField()
    
    class Meta:
        ordering = ('name',)

    def discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        discounted_price = self.price - discount_amount
        return discounted_price
    

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE)
    # NOT NULL constraint failed: products_userprofile.products_id
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username} {self.products.name}"
# check if the user is in the database and raise error.

    def clean(self):
        existing_user = UserProfile.objects.filter(
            user=self.user).exclude(pk=self.pk)
        if existing_user.exists():
            raise ValidationError("A user with this name already exists.")


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    # last_modified = models.DateTimeField(auto_now=True,default=None)

    def __str__(self):
        return f"cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

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
        return f"Order # {self.pk} for {self.user}"


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is selling{self.products} with {self.category}"

    class Meta:
        ordering = ['date_added']


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:  # If it's a new instance
            self.delivery_date = datetime.now() + timedelta(days=5)
        super().save(*args, **kwargs)

from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transactions_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

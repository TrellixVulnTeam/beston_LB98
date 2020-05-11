from rest_framework import serializers

from store.models import *
from web.models import *


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ShippingAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

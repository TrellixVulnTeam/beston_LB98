from django.contrib import admin

from store.models import *

admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
from django.contrib import admin
from .models import Inventory, Order, OrderItem, Shipping

admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)

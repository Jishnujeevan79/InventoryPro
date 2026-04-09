from django.contrib import admin
from .models import Product, Order, OrderItem, Manufacturing

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Manufacturing)# Register your models here.

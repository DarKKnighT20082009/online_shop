from django.contrib import admin

from order.models import Address, Coupon, Order, OrderItem

# Register your models here.

admin.site.register(Address)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
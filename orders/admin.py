from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'is_paid', ]

    inlines = [
        OrderItemInLine
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]

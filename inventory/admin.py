from django.contrib import admin
from inventory.models import (
    Customer,
    ProductType,
    Product,
    Transaction,
    LineItem,
    PaymentOption,
    Order,
)

@admin.register(PaymentOption)
class PaymentOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'date_created', 'date_paid', 'weight',
        'date_claimed', 'date_required', 'remarks', 'payment_status')


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'product', 'quantity', 'price_override')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'product_type', 'unit_price', 'date_created')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'customer',)

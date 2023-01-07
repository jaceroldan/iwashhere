from decimal import Decimal

from django.db import models
from django.db.models import Sum


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class ProductType(models.Model):
    name = models.CharField(max_length = 256)

    def __str__(self):
        return f'Product Type: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(null=True, blank=True)
    product_type = models.ForeignKey(
        ProductType, related_name='products', on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name} @ PHP {self.unit_price} ({self.quantity} remaining)'


class PaymentOption(models.Model):
    name = models.CharField(max_length=100)


class Invoice(models.Model):
    is_paid = models.BooleanField(default=False)
    

class Transaction(models.Model):
    NOT_PAID = 0
    DOWNPAYMENT_RECEIVED = 1
    FULLY_PAID = 2
    PAYMENT_STATUSES = (
        (NOT_PAID, 'Not paid'),
        (DOWNPAYMENT_RECEIVED, 'Downpayment received'),
        (FULLY_PAID, 'Fully paid'),
    )

    customer = models.ForeignKey(
        Customer, related_name='transactions', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateTimeField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    date_claimed = models.DateTimeField()
    date_required = models.DateTimeField()
    payment_option = models.OneToOneField(
        PaymentOption, related_name='payment_option', on_delete=models.CASCADE)
    payment_status = models.IntegerField(choices=PAYMENT_STATUSES, default=NOT_PAID)
    remarks = models.TextField()

    def __str__(self):
        return f'Transaction by {self.customer} on {self.date_created}'

    @property
    def total_price(self):
        price = 0.0
        for item in self.line_items.iterate():
            price += item.total_price
        return price


class LineItem(models.Model):
    transaction = models.ForeignKey(
        Transaction, related_name='line_items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='line_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_override = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    @property
    def total_price(self):
        if self.price_override:
            return self.price_override
        return self.quantity * self.product.unit_price


class Order(models.Model):
    UNPAID = 0
    CASH = 1
    GCASH = 2
    PAYMENT_METHOD_CHOICES = (
        (UNPAID, 'Unpaid'),
        (CASH, 'Cash'),
        (GCASH, 'GCash')
    )

    date_created = models.DateTimeField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orders')
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    remarks = models.TextField()
    wash_cost = models.DecimalField(max_digits=8, decimal_places=2)
    dry_cost = models.DecimalField(max_digits=8, decimal_places=2)
    detergent_cost = models.DecimalField(max_digits=8, decimal_places=2)
    fabcon_cost = models.DecimalField(max_digits=8, decimal_places=2)
    bleach_cost = models.DecimalField(max_digits=8, decimal_places=2)
    plastic_cost = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD_CHOICES, default=CASH)
    payment_made = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0.0))
    date_required = models.DateTimeField(null=True, blank=True)
    date_claimed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer}: {self.date_created}'

    @property
    def service_cost(self):
        return self.wash_cost + self.dry_cost

    @property
    def total_cost(self) -> Decimal:
        return (
            self.service_cost
            + self.detergent_cost
            + self.fabcon_cost
            + self.bleach_cost
            + self.plastic_cost
        )

    @property
    def payment_method_display(self) -> str:
        return self.get_payment_method_display()

    @property
    def payment_status(self) -> str:
        return (
            'Paid' if self.payment_made >= self.total_cost else 'Unpaid'
            + f' {self.payment_method_display}')

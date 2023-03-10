# Generated by Django 4.1.4 on 2023-01-05 09:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_order_num_of_serviced_dry_loads_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_made',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_remove_order_service_cost_order_dry_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

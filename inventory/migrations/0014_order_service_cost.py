# Generated by Django 4.1.4 on 2023-02-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_alter_customer_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]

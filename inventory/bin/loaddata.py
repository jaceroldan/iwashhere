from datetime import datetime
import csv

from inventory.models import Order, Customer

with open('./inventory/fixtures/data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        customer, _ = Customer.objects.get_or_create(first_name=row[2],)
        date_created = datetime.strptime(row[1], '%m-%d').replace(year=2023)
        if row[12] and row[13]:
            date_required = datetime.strptime(f'{row[12]} {row[13]}', "%d-%b %H %p").replace(year=2023)
        if row[14] and row[15]:
            date_claimed = datetime.strptime(f'{row[14]} {row[15]}', "%d-%b %H:%M").replace(year=2023)
        payment_method = Order.UNPAID
        if row[11] == 'Paid':
            payment_method = Order.CASH
        elif row[11] == 'GCash':
            payment_method = Order.GCASH

        Order.objects.create(
            date_created=date_created,
            customer=customer,
            weight=row[3] or 0.0,
            remarks=row[4],
            service_cost=row[5] or 0.0,
            detergent_cost=row[6] or 0.0,
            fabcon_cost=row[7] or 0.0,
            bleach_cost=row[8] or 0.0,
            plastic_cost=row[9] or 0.0,
            payment_method=payment_method,
            date_required=date_required,
            date_claimed=date_claimed,
        )

import json

from django.utils import timezone

from django.core.serializers import serialize
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render, redirect

from inventory.models import Customer, Order

# Create your views here.
def show_create_receipt(request):
    return render(request, 'inventory/create_order_slip.html')


def show_edit_receipt(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {
        'order': order
    }
    return render(request, 'inventory/edit_order_slip.html', context)


def show_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {'order': order}
    return render(request, 'inventory/view_order.html', context)


def create_receipt(request):
    customer = request.POST['customer']
    contact_number = request.POST['contact_number']
    customer = Customer.objects.create(
        first_name=customer,
        contact_number=contact_number
    )

    weight = request.POST['weight']
    # TODO: What do I do with this?
    # service_type = request.POST['service_type']
    wash_cost = request.POST['wash_cost']
    dry_cost = request.POST['dry_cost']
    # TODO: Ask about the fold cost
    # fold_cost = request.POST['fold_cost']
    detergent_cost = request.POST['detergent_cost']
    fabcon_cost = request.POST['fabcon_cost']
    bleach_cost = request.POST['bleach_cost']
    bleach_cost = request.POST['bleach_cost']
    plastic_cost = request.POST['plastic_cost']
    date_required = request.POST['date_required']
    time_required = request.POST['time_required']

    date_required = datetime.strptime(f'{date_required} {time_required}', '%Y-%m-%d %H:%M')

    Order.objects.create(
        customer=customer,
        weight=weight,
        wash_cost=wash_cost,
        dry_cost=dry_cost,
        # fold_cost=fold_cost,
        detergent_cost=detergent_cost,
        fabcon_cost=fabcon_cost,
        bleach_cost=bleach_cost,
        plastic_cost=plastic_cost,
        date_required=date_required
    )

    return redirect('inventory:list')


def update_receipt(request, order_id):
    order = Order.objects.get(pk=order_id)
    customer = order.customer
    
    first_name = request.POST['customer']
    contact_number = request.POST['contact_number']
    customer.first_name = first_name
    customer.contact_number = contact_number
    customer.save(update_fields=['first_name', 'contact_number'])

    order.weight = request.POST['weight']
    order.wash_cost = request.POST['wash_cost']
    order.dry_cost = request.POST['dry_cost']
    order.detergent_cost = request.POST['detergent_cost']
    order.fabcon_cost = request.POST['fabcon_cost']
    order.bleach_cost = request.POST['bleach_cost']
    order.plastic_cost = request.POST['plastic_cost']
    date_required = request.POST['date_required']
    time_required = request.POST['time_required']

    order.date_required = datetime.strptime(f'{date_required} {time_required}', '%Y-%m-%d %H:%M')
    order.save()

    return redirect('inventory:list-orders')


def mark_as_claimed_receipt(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.date_claimed = timezone.now()
    order.save(update_fields=['date_claimed'])
    return redirect('inventory:view', order_id)


def mark_as_paid_receipt(request, order_id):
    order = Order.objects.get(pk=order_id)
    print(request.POST)
    order.payment_made = request.POST['payment_amount']
    order.payment_method = request.POST['payment_option']
    order.save(update_fields=['payment_made', 'payment_method'])
    return redirect('inventory:view', order_id)


def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'inventory/orders_list.html', context)


def list_unclaimed_orders(request):
    unclaimed_orders = Order.objects.filter(date_claimed__isnull=True)
    context = {
        'orders': unclaimed_orders
    }
    return render(request, 'inventory/orders_list.html', context)

def retrieve_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {
        'obj': {
            'order': serialize('json', [order]),
            'customer': serialize('json', [order.customer]),
        }
    }
    return HttpResponse(json.dumps(context))


def list_customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'inventory/customers_list.html', context)

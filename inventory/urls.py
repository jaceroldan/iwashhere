from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('order/new/', views.show_create_receipt, name='new'),
    path('order/create/', views.create_receipt, name='create'),
    path('order/view/<int:order_id>', views.show_order, name='view'),
    path('order/json/<int:order_id>', views.retrieve_order, name='order_json'),
    path('orders/', views.list_orders, name='list-orders'),
    path('customers/', views.list_customers, name='list-customers'),
]

from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.show_menu, name='menu'),
    path('order/new/', views.show_create_receipt, name='new'),
    path('order/create/', views.create_receipt, name='create'),
    path('order/edit/<int:order_id>', views.show_edit_receipt, name='edit'),
    path('order/update/<int:order_id>', views.update_receipt, name='update'),
    path('order/mark-paid/<int:order_id>', views.mark_as_paid_receipt, name='mark-paid'),
    path('order/mark-claimed/<int:order_id>', views.mark_as_claimed_receipt, name='mark-claimed'),
    path('order/view/<int:order_id>', views.show_order, name='view'),
    path('order/json/<int:order_id>', views.retrieve_order, name='order-json'),
    path('orders/', views.list_orders, name='list-orders'),
    path('orders-unclaimed/', views.list_unclaimed_orders, name='list-orders-unclaimed'),
    path('customers/', views.list_customers, name='list-customers'),
]

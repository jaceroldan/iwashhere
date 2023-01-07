from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('order/new/', views.show_create_receipt, name='new'),
    path('order/create/', views.create_receipt, name='create'),
    path('order/view/<int:order_id>', views.show_order, name='view'),
    path('list/', views.list_customers, name='list-orders'),
]

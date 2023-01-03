from django.urls import path

from . import views

urlpatterns = [
    path('receipt/new/', views.create_receipt, name='new'),
]

from django.shortcuts import render

# Create your views here.
def create_receipt(request):
    return render(request, 'inventory/receipt.html')

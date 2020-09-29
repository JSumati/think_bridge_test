from django.shortcuts import render
from .models import inventory
from django.http import HttpResponse


def list_inventory(request):
    inventories = inventory.objects.all()
    return render(request, 'inventory.html',{'inventories': inventories})

def show_inventory():
    pass

def add_inventory(request):
    return HttpResponse(request)

def delete_inventory():
    pass




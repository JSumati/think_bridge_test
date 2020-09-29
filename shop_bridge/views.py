from django.shortcuts import render
from .models import inventory


def list_inventory():
    inventories = inventory.objects.all()
    return inventories

def show_inventory():
    pass

def add_inventory():
    pass

def delete_inventory():
    pass




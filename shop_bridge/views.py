from django.shortcuts import render, redirect
from .models import inventory
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers
import json



@api_view(['GET'])
def list_inventory(request):
    inventories = inventory.objects.all()
    return render(request, 'index.html',{'inventories': inventories})

@api_view(['GET'])
def show_inventory(request, id):
    record = inventory.objects.filter(id = id)
    return render(request, 'show.html',{'record': record})

@api_view(['POST'])
def add_inventory(request):
    data = inventory(name = request.POST.get('name'), price = request.POST.get('price'), description = request.POST.get('description'), image = request.FILES['img'])
    data.save()
    return redirect('/inventory')

@api_view(['POST'])
def delete_inventory(request, id):
    data = inventory.objects.filter(id = id).delete()
    return redirect('/inventory')
from django.shortcuts import render, redirect
from .models import inventory
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_inventory(request):
    inventories = inventory.objects.all()
    return render(request, 'index.html',{'inventories': inventories})

@api_view(['GET'])
def show_inventory(request, id):
    if request.method == 'GET':
        record = inventory.objects.filter(id = id)
        return render(request, 'show.html',{'record': record})

# @api_view(['POST'])
def add_inventory(request):
    if request.method == 'POST':
        data = inventory(name = request.POST.get('name'), price = request.POST.get('price'), description = request.POST.get('description'), image = request.FILES['img'])
        data.save()
        return redirect('/inventory')

@api_view(['POST'])
def delete_inventory(request, id):
    # if request.method == 'DELETE':
    data = inventory.objects.filter(id = id).delete()
    return redirect('/inventory')
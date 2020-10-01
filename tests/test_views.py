from django.test import RequestFactory
from django.urls import reverse
from shop_bridge.views import *
import pytest
from django.test import TestCase
import json
from PIL import Image


@pytest.mark.django_db
class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_inventory_list(self):
        path = reverse('list')
        request = self.factory.get(path)

        response = list_inventory(request)
        assert response.status_code == 200

    def test_inventory_show(self):
        path = reverse('show', kwargs={'id':10})
        request = self.factory.get(path)

        response = show_inventory(request, id=10)
        self.assertEqual(response.charset, 'utf-8') 

    def test_inventory_add(self):
        path = reverse('add')
        image = Image.new('RGB', (200, 200), 'white')
        body = {'name': 'test name', 'price' :123, 'description' :'test description'}
        request = self.factory.post(path, body, enctype='multipart/form-data')
        request.FILES['img'] = image

        response = add_inventory(request)
        assert response.status_code == 200

    def test_inventory_remove(self):
        path = reverse('remove', kwargs = {'id':10})
        request = self.factory.post(path)
        
        response = delete_inventory(request, id=10)
        assert response.status_code == 302

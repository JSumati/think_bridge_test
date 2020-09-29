from django.urls import path
from . import views

urlpatterns = [
    path('/',views.list_inventory),
    path('/show/<int:id>', views.show_inventory),
    path('/add', views.add_inventory),
    path('/remove/<int:id>', views.delete_inventory)
]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.list_inventory, name = 'list'),
    path('<int:id>', views.show_inventory, name = 'show'),
    path('add', views.add_inventory, name='add'),
    path('remove/<int:id>', views.delete_inventory, name = 'remove')

]

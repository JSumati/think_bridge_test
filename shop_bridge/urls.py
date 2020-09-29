from django.urls import path
from . import views


urlpatterns = [
    path('',views.list_inventory),
    path('<int:id>', views.show_inventory, name = 'show'),
    path('add', views.add_inventory),
    path('remove/<int:id>', views.delete_inventory, name = 'remove')

]

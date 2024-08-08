from django.urls import path
from . import views

urlpatterns = [
    path("", views.inventory_list, name="inventory_list"),
    path("<uuid:pk>/", views.inventory_detail, name="inventory_detail"),
    path("new/", views.inventory_create, name="inventory_create"),
    path("<uuid:pk>/edit/", views.inventory_update, name="inventory_update"),
    path("<uuid:pk>/delete/", views.inventory_delete, name="inventory_confirm_delete"),
]

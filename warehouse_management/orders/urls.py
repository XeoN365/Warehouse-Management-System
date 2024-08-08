from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("<uuid:pk>/", views.order_detail, name="order_detail"),
    path("new/", views.order_create, name="order_create"),
    path("<uuid:pk>/edit/", views.order_update, name="order_update"),
    path("<uuid:pk>/delete/", views.order_delete, name="order_confirm_delete"),
    path("<uuid:pk>/shipping/", views.shipping_create, name="shipping_create"),
]

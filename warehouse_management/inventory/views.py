from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm
import uuid


def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, "inventory/inventory_list.html", {"items": items})


def inventory_detail(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    return render(request, "inventory/inventory_detail.html", {"item": item})


def inventory_create(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("inventory_list")
    else:
        form = InventoryForm()
    return render(request, "inventory/inventory_form.html", {"form": form})


def inventory_update(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("inventory_detail", pk=item.pk)
    else:
        form = InventoryForm(instance=item)
    return render(request, "inventory/inventory_form.html", {"form": form})


def inventory_delete(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("inventory_list")
    return render(request, "inventory/inventory_confirm_delete.html", {"item": item})

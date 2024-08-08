from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Shipping
from .forms import OrderForm, ShippingForm


def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    shipping_details = Shipping.objects.get(order=order)
    return render(
        request,
        "orders/order_detail.html",
        {"order": order, "shipping_details": shipping_details},
    )


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/order_form.html", {"form": form})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(request, "orders/order_delete_confirm.html", {"order": order})


def shipping_create(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.order = order
            shipping.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = ShippingForm()
    return render(request, "orders/shipping_form.html", {"form": form})

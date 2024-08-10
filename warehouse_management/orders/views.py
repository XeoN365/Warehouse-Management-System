from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Shipping
from .forms import OrderForm, ShippingForm
from django.contrib.auth.decorators import login_required


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    try:
        shipping_details = Shipping.objects.get(order=order)
    except:
        shipping_details = None
    return render(
        request,
        "orders/order_detail.html",
        {"order": order, "shipping_details": shipping_details},
    )


@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})


@login_required
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


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(request, "orders/order_confirm_delete.html", {"order": order})


@login_required
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
    return render(request, "orders/shipping_form.html", {"form": form, "order": order})

from django.db import models
import uuid


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=10, unique=True)
    sku = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Inventory, through="OrderItem")

    def __str__(self):
        return f"Order #{self.order_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return (
            f"{self.quantity}x {self.inventory.name} (Order #{self.order.order_number})"
        )


class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pending")
    tracking_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Shipping for Order #{self.order.order_number}"

from django.db import models
import uuid


# Inventory aka Item Model
class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=10, unique=True)
    sku = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

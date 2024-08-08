from django import forms
from .models import Inventory


# Set up form for adding new inventory item
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "description", "quantity", "location", "sku"]

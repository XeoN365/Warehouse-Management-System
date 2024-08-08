from django import forms
from .models import Order, Shipping


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_email", "items"]
        widgets = {
            "customer_name": forms.TextInput(
                attrs={"placeholder": "Enter customer's name"}
            ),
            "customer_email": forms.EmailInput(
                attrs={"placeholder": "Enter customer's email"}
            ),
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = [
            "address",
            "city",
            "state",
            "postal_code",
            "country",
            "tracking_number",
        ]

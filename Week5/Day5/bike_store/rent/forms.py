from django import forms
from .models import Rental, Customer, Vehicle

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['rental_date', 'return_date', 'customer', 'vehicle']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'date_created', 'real_cost', 'size']

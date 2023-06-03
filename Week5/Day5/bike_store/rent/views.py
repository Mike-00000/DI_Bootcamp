from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Rental, Customer, Vehicle, VehicleType, VehicleSize
from .forms import RentalForm, CustomerForm, VehicleForm

# Create your views here.

class RentalListView(generic.ListView):
    model = Rental
    template_name = 'rental_list.html'
    ordering = ['return_date__isnull', 'return_date']

class RentalDetailView(generic.DetailView):
    model = Rental
    template_name = 'rental_detail.html'

class RentalCreateView(generic.CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'rental_create.html'

class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'customer_list.html'
    ordering = ['last_name', 'first_name']

class CustomerCreateView(generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create.html'

class VehicleGroupListView(generic.ListView):
    model = VehicleType
    template_name = 'vehicle_group_list.html'

class VehicleDetailView(generic.DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'

class VehicleCreateView(generic.CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_create.html'

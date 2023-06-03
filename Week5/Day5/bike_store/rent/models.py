from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)
    real_cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE) 
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_type.name} - {self.size.name}"

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rental: {self.rental_date} to {self.return_date} (Customer: {self.customer}, Vehicle: {self.vehicle})"

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type} - {self.vehicle_size}: {self.daily_rate} per day"


class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class RentalStation(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
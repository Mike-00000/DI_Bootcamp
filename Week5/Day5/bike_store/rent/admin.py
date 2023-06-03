from django.contrib import admin
from .models import VehicleType, VehicleSize, RentalRate, Customer, Rental, Vehicle, Address, RentalStation

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country')
    ordering = ('last_name',)

admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(RentalRate)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental)
admin.site.register(Vehicle)
admin.site.register(Address)
admin.site.register(RentalStation)


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Rental, Customer, VehicleSize, VehicleType, Vehicle, RentalRate
from faker import Faker
import random
from datetime import datetime, timedelta
from django.utils import timezone

fake = Faker()

vehicles = Vehicle.objects.all()


def create_rentals(num_rentals):
    # Filter available vehicles
    vehicles = Vehicle.objects.filter(rental__isnull=True, return_date__isnull=True)
    print(f"Number of available vehicles: {vehicles.count()}")


    for _ in range(num_rentals):
        # Generate random data
        start_date = timezone.now() - timedelta(days=30)
        end_date = timezone.now()
        rental_date = fake.date_between_dates(start_date, end_date)

        return_date = None
        if random.choice([True, False]):
            return_date = fake.date_between_dates(rental_date, end_date)

        # Check if vehicle is available
        vehicle = random.choice(vehicles)

        # Create rental
        customer = Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country()
        )

        try:
            Rental.objects.create(
                rental_date=rental_date,
                return_date=return_date,
                customer=customer,
                vehicle=vehicle,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
        except Exception as e:
            print(f"An error occurred while creating rental: {e}")

if __name__ == '__main__':
    create_rentals(100)

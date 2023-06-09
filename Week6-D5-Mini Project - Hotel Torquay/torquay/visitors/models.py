from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    surface = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.guest_name} - Room {self.room.room_number}"

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.guest_name} - Rating: {self.rating}"

from django.db import models

class Parking(models.Model):
    vehicle_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100)
    flat_number = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=20, choices=[('Car', 'Car'), ('Bike', 'Bike')])
    slot_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.vehicle_number} - Slot {self.slot_number}"

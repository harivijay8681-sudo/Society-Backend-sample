from django.db import models

class FireSafetyEquipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    last_inspection_date = models.DateField()
    next_inspection_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('OK', 'OK'), ('Needs Attention', 'Needs Attention')])

    def __str__(self):
        return f"{self.equipment_name} - {self.location}"

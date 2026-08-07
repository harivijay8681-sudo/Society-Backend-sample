from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    flat_number = models.CharField(max_length=10)
    purpose = models.CharField(max_length=200)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.flat_number}"

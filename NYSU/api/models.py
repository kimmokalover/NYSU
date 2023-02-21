from django.db import models

class User(models.Model):
    license_plate = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    first_responder = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, default = '')
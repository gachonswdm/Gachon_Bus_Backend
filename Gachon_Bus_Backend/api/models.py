from django.db import models

class location(models.Model):
    bus_id = models.CharField(max_length=30)
    phone_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
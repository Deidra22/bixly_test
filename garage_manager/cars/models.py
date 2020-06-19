from django.db import models
import uuid
from django.contrib import admin
from garage_manager.choices import carTruckMakeModelChoices, carTruckSeatChoices


class Cars(models.Model):
    class Meta:
        verbose_name_plural = 'Cars'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default="VIN NUMBER")
    current_mileage = models.IntegerField(blank=False, null=True)

    make = models.CharField(
        max_length=10,
        choices=carTruckMakeModelChoices.MAKE,
        default='Acura',
    )

    seats = models.IntegerField(
        verbose_name='Number of Seats', 
        choices=carTruckSeatChoices.choices,
        default='2'
    )

class CarsAdmin(admin.ModelAdmin):

   list_display = ('id', 'vin', 'make', 'seats','current_mileage')


from django.db import models
import uuid
from django.contrib import admin
from garage_manager.choices import carTruckMakeChoices, carModelChoices ,carTruckSeatChoices

class Cars(models.Model):
    class Meta:
        verbose_name_plural = 'Cars'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default=None)
    current_mileage = models.IntegerField(blank=False, null=True)

    make = models.CharField(max_length=20, choices=carTruckMakeChoices.MAKE_CHOICES, default='Acura')
    model = models.CharField(max_length=20, choices=carModelChoices.CAR_MODELS, default=None)
    seats = models.CharField(max_length=20, choices=carTruckSeatChoices.SEAT_CHOICES, default='2')


class CarsAdmin(admin.ModelAdmin):

   list_display = ('id', 'vin', 'make', 'model', 'seats','current_mileage')


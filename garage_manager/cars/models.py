from django.db import models
import datetime
import uuid
from django.contrib import admin
from garage_manager.choices import carTruckMakeChoices, carModelChoices, carTruckSeatChoices, carTruckServiceInterval, carTruckColorChoices

class Cars(models.Model):
    class Meta:
        verbose_name_plural = 'Cars'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default=None)

    current_mileage = models.IntegerField(blank=False, null=True)
    year = models.IntegerField(default=None, blank=False)

    make = models.CharField(max_length=20, choices=carTruckMakeChoices.MAKE_CHOICES, default='Chevrolet')
    model = models.CharField(max_length=20, choices=carModelChoices.CAR_MODELS, default=None)
    seats = models.CharField(max_length=20, choices=carTruckSeatChoices.SEAT_CHOICES, default='2')
    color = models.CharField(max_length=6, choices=carTruckColorChoices.COLOR_CHOICES, default=None)
    service_interval = models.CharField(max_length=10, choices=carTruckServiceInterval.SERVICE_INTERVAL, default='3 Months')

    next_service = models.DateField(verbose_name='Next Service Date')

class CarsAdmin(admin.ModelAdmin):

   list_display = ('id', 'vin', 'make', 'model', 'color', 'seats','current_mileage', 'service_interval', 'next_service')


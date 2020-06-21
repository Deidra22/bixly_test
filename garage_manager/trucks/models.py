from django.db import models
from datetime import date
import uuid
from django.contrib import admin
from garage_manager.choices import carTruckMakeChoices, truckModelChoices, carTruckSeatChoices, carTruckServiceInterval, truckBedLength


class Trucks(models.Model):
    class Meta:
        verbose_name_plural = 'Trucks'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default=None)
    current_mileage = models.IntegerField(blank=False, null=True)

    make = models.CharField(max_length=20, choices=carTruckMakeChoices.MAKE_CHOICES, default='Chevrolet')
    model = models.CharField(max_length=20, choices=truckModelChoices.TRUCK_MODELS, default=None)
    seats = models.CharField(max_length=20, choices=carTruckSeatChoices.SEAT_CHOICES, default='2')
    bed_length = models.CharField(max_length=6, choices=truckBedLength.BED_LENGTH, default='5 ft')
    service_interval = models.CharField(max_length=12, choices=carTruckServiceInterval.SERVICE_INTERVAL, default='3 Months')
    next_service = models.DateField(verbose_name='Next Service Date')


class TrucksAdmin(admin.ModelAdmin):
     list_display = ('id', 'vin', 'make', 'model', 'seats','current_mileage', 'service_interval', 'next_service')

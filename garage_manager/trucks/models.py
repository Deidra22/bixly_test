from django.db import models
from datetime import date
import uuid
from django.contrib import admin
from garage_manager.choices import CarTruckMakeChoices, TruckModelChoices, CarTruckSeatChoices, CarTruckServiceInterval, TruckBedLength, CarTruckColorChoices


class Trucks(models.Model):
    class Meta:
        verbose_name_plural = 'Trucks'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default=None)

    current_mileage = models.IntegerField(blank=False, null=True)
    year = models.IntegerField(default=None, blank=False)

    make = models.CharField(max_length=20, choices=CarTruckMakeChoices.MAKE_CHOICES, default='Chevrolet')
    model = models.CharField(max_length=20, choices=TruckModelChoices.TRUCK_MODELS, default=None)
    seats = models.CharField(max_length=20, choices=CarTruckSeatChoices.SEAT_CHOICES, default='2')
    bed_length = models.CharField(max_length=6, choices=TruckBedLength.BED_LENGTH, default='5ft')
    color = models.CharField(max_length=6, choices=CarTruckColorChoices.COLOR_CHOICES, default=None)
    service_interval = models.CharField(max_length=12, choices=CarTruckServiceInterval.SERVICE_INTERVAL, default='3 Months')

    next_service = models.DateField(verbose_name='Next Service Date')


class TrucksAdmin(admin.ModelAdmin):
     list_display = ('id', 'vin', 'make', 'model', 'year', 'color', 'seats','current_mileage', 'service_interval', 'next_service')

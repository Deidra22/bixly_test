from django.db import models
import uuid
from django.contrib import admin
from .choices import BoatMakeChoices, BoatModelChoices, BoatLengthChoices, BoatWidthChoices, BoatServiceInterval

class Boats(models.Model):
    class Meta:
        verbose_name_plural = 'Boats'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hin = models.CharField(max_length=12, verbose_name='HIN', default=None)

    current_hours = models.IntegerField(blank=False, null=True)
    year = models.IntegerField(default=None, blank=False)

    make = models.CharField(max_length=15, choices=BoatMakeChoices.MAKE_CHOICES, default='Caymas Boats')
    model = models.CharField(max_length=15, choices=BoatModelChoices.MODEL_CHOICES, default=None)
    length = models.CharField(max_length=4, choices=BoatLengthChoices.LENGTH_CHOICES, default='14ft')
    width = models.CharField(max_length=4, choices=BoatWidthChoices.WIDTH_CHOICES, default='60in')
    service_interval = models.CharField(max_length=10, choices=BoatServiceInterval.SERVICE_INTERVAL, default='6 Months')

    next_service = models.DateField(verbose_name='Next Service Date')

class BoatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hin', 'make', 'model', 'year','length', 'width', 'current_hours', 'service_interval', 'next_service']

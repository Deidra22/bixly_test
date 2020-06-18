from django.db import models
from django.contrib import admin
import uuid

class Cars(models.Model):
    class Meta:
        verbose_name_plural = 'Cars'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vin = models.CharField(max_length=17, default="VIN NUMBER")
    current_mileage = models.IntegerField(blank=False, null=True)

class CarsAdmin(admin.ModelAdmin):
   list_display = ('id', 'vin', 'current_mileage')
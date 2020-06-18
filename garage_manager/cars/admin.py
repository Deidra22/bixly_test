from django.contrib import admin
from .models import Cars, CarsAdmin

admin.site.register(Cars, CarsAdmin)

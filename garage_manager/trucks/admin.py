from django.contrib import admin
from .models import Trucks, TrucksAdmin

admin.site.register(Trucks, TrucksAdmin)

from django.contrib import admin
from .models import Boats, BoatsAdmin

admin.site.register(Boats, BoatsAdmin)

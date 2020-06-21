from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .api import CarViewSet
from .api import TruckViewSet
from .api import BoatViewSet


router = routers.DefaultRouter()
router.register(r'api/cars', CarViewSet)
router.register(r'api/trucks', TruckViewSet)
router.register(r'api/boats', BoatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
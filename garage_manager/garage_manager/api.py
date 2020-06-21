from rest_framework import viewsets, permissions

from cars.serializers import CarSerializer
from cars.models import Cars

from trucks.serializers import TruckSerializer
from trucks.models import Trucks

from boats.serializers import BoatSerializer
from boats.models import Boats

# Cars viewset
class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

# Trucks viewset
class TruckViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TruckSerializer

# Boats viewset
class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boats.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoatSerializer 
from rest_framework import viewsets, permissions
from .serializers import CarSerializer
from cars.models import Cars

# Cars viewset

class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer
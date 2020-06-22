from rest_framework import serializers
from trucks.models import Trucks

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = '__all__'
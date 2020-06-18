from rest_framework import serializers
from cars.models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
from rest_framework import serializers
from boats.models import Boats

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boats
        fields = '__all__'
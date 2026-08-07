from rest_framework import serializers
from .models import FireSafetyEquipment

class FireSafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = FireSafetyEquipment
        fields = '__all__'

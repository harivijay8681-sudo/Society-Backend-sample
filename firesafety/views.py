from rest_framework import viewsets
from .models import FireSafetyEquipment
from .serializers import FireSafetySerializer

class FireSafetyViewSet(viewsets.ModelViewSet):
    queryset = FireSafetyEquipment.objects.all()
    serializer_class = FireSafetySerializer

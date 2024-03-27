from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related('brand').all()
    serializer_class = CarSerializer

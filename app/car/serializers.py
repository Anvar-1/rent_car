from rest_framework import serializers
from app.brand.serializers import BrandSerializer
from app.brand.models import Brand
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Brand.objects.all(), source='id')

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car.objects.create(brand=validated_data.pop('id'), **validated_data)

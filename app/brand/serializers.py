from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    class PictureSerialiser(serializers.ModelSerializer):
        creator = serializers.ReadOnlyField(source='creator.username')
        creator_id = serializers.ReadOnlyField(source='creator.id')
        image_url = serializers.SerializerMethodField('get_image_url')
        
    def get_image_url(self, obj):
        return obj.image.url
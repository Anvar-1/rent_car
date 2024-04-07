from rest_framework import serializers
from .models import BlogModel

class BlogModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = BlogModel
        fields = '__all__'
    
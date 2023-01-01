from rest_framework import serializers
from .models import ImgProject
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgProject
        fields = ('__all__')
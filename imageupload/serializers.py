from rest_framework import serializers
from .models import *


class UploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `ImageUpload` instance, given the validated data.
        """
        return ImageUpload.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

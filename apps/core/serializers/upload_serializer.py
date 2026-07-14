from rest_framework import serializers
from apps.core.services.upload import DataService

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    data = serializers.JSONField()

    def create(self, validated_data):
        return DataService.create_data(validated_data)

class UploadSerializer(serializers.Serializer):
    """Jittered upload uchun maxsus serializer"""
    task_type = serializers.CharField(max_length=50, default="db_sync")
    data = serializers.JSONField()
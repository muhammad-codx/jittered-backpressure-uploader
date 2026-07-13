from rest_framework import serializers

class UploadDataSerializer(serializers.Serializer):
    task_type = serializers.CharField(max_length=50, default="db_sync")
    payload = serializers.JSONField()

    def validate_task_type(self, value):
        allowed_types = ["db_sync", "heavy_upload"]
        if value not in allowed_types:
            raise serializers.ValidationError(f"task_type faqat shulardan biri bo'lishi mumkin: {allowed_types}")
        return value
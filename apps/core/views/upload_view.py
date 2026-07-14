from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from apps.core.serializers.upload_serializer import DataSerializer, UploadSerializer
from apps.core.services.upload import JitteredBackpressureService

class DataAPIView(APIView):
    @extend_schema(
        summary="Ma'lumot yaratish",
        description="Yangi data modelini bazaga saqlash.",
        request=DataSerializer,
        responses={201: DataSerializer}
    )
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadView(APIView):
    @extend_schema(
        summary="Kechiktirilgan yuklash (Backpressure)",
        description="Jitter algoritmi yordamida server yuklamasini boshqarish.",
        request=UploadSerializer,
        responses={201: {"status": "ok"}, 400: {"error": "Validatsiya xatosi"}}
    )
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        task_type = serializer.validated_data['task_type']
        data = serializer.validated_data['data']
        
        try:
            success = JitteredBackpressureService.upload_data(task_type, data)
            if success:
                return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"error": "Upload failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
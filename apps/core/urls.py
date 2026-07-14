from django.urls import path
from apps.core.views.upload_view import UploadView,DataAPIView

app_name = "core"


urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload"),
    path("data/", DataAPIView.as_view(), name="data"),
]
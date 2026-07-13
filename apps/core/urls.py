from django.urls import path
from .views.upload_view import UploadView
app_name = "core"

urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload"),
]

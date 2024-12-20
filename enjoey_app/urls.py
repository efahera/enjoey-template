from django.urls import path
from .views import UploadCSVView
from .viewsChildren import UploadCSVViewChildren

urlpatterns = [
    path('upload-csv-staff/', UploadCSVView.as_view(), name='upload_csv_staff'),
    path('upload-csv-children/', UploadCSVViewChildren.as_view(), name='upload_csv_children'),
]

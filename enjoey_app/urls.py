from django.urls import path
from .viewsStaff import UploadCSVView
from .viewsChildren import UploadCSVViewChildren

urlpatterns = [
    path('upload-csv-staff/', UploadCSVView.as_view(), name='upload_csv_staff'),
    path('upload-csv-children/', UploadCSVViewChildren.as_view(), name='upload_csv_children'),
# conversion-staff
# create new views for staff
]

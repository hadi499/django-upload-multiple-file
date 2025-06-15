from django.urls import path
from .views import upload_download_view, download_file, delete_file

urlpatterns = [
    path('', upload_download_view, name='upload_download'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
]
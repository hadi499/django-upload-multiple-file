from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from .models import Document
import os
from django.conf import settings

def upload_download_view(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:
            Document.objects.create(file=file)
        return redirect('upload_download')  # agar tidak repost saat refresh

    documents = Document.objects.all()
    return render(request, 'upload_download.html', {'documents': documents})

def download_file(request, file_id):
    try:
        document = Document.objects.get(id=file_id)
        file_path = document.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    except Document.DoesNotExist:
        raise Http404("File tidak ditemukan.")

def delete_file(request, file_id):
    document = get_object_or_404(Document, id=file_id)
    
    # Hapus file dari sistem file (storage)
    file_path = document.file.path
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Hapus dari database
    document.delete()
    return redirect('upload_download')
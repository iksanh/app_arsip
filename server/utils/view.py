from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os


from django.http import FileResponse, Http404

def view_pdf(request):
    file_path = settings.MEDIA_ROOT / 'matriks.pdf'  # Update 'filename.pdf' to the actual filename
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline;filename={file_path}'
        return response


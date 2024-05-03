import json
from io import BytesIO
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

from dokumen.models import DokumenModel 
from arsip.models import ArsipModel
from arsip.api.serializers import FilteredArsipSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view




from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle




# Create your views here.

def detail_report(request):
   keterangan = ['SURAT MASUK', 'SURAT KELUAR', 'LAINNYA']
   
   context  = {
      'data' : '',
      'modul' : 'Laporan Detail', 
      'links' : {
        'create': 'create-dokumen',
        'delete': 'delete-dokumen',
        'edit': 'edit-dokumen',
      
      }, 
      'parameter': {
        'report' : True,
        'detail': True
      },
      'dokumen': DokumenModel.objects.all(),
      'keterangan': keterangan
    }

   

   if request.method == 'POST':
      query_set = ArsipModel.objects.all()
      q_object = Q()

      dokumen = request.POST.get('dokumen')
      keterangan = request.POST.get('keterangan')
      periode = request.POST.get('periode_laporan')

      if dokumen and dokumen != 'Pilih Dokumen':
         query_set = ArsipModel.objects.all()
         q_object &= Q(jenis_dokumen=dokumen)
         
      
      if keterangan and keterangan != 'Pilih Keterangan':
         query_set = ArsipModel.objects.all()
         q_object &= Q(keterangan=keterangan)

      if periode: 
         start_date, end_date = periode.split(' - ')
         start_date = datetime.strptime(start_date.strip(), '%m/%d/%Y').date()
         end_date = datetime.strptime(end_date.strip(), '%m/%d/%Y').date()
         q_object &= Q(tanggal_dokumen__range=(start_date, end_date))
      
      query_set = query_set.filter(q_object)
      # Add additional filters for other parameters as needed
      
      print(dokumen, keterangan, periode)
      # Print SQL query
      print(query_set.query)
      
      tanggal_mulai , tanggal_selesai = periode.split('-')
      context['data'] = query_set
      context['dokumen_value'] = dokumen
      context['keterangan_value'] = keterangan
      context['tanggal_mulai'] = tanggal_mulai
      context['tanggal_selesai'] = tanggal_selesai
      
      return render(request, 'report_view.html', context)   
   context['data'] =  ArsipModel.objects.none()
   return render(request, 'report_view.html', context)




@csrf_exempt
def detail_report_get(request):
   if request.method == 'POST':
      data = json.loads(request.body.decode('utf-8'))
      dokumen = data.get('dokumen')
      keterangan = data.get('keterangan')
      periode = data.get('periode')

      data  = {
         'dokumen' : dokumen,
         'keterangan' : keterangan,
         'periode': periode
      }

      # Filter ArsipModel objects based on the received parameters
      arsip_query = ArsipModel.objects.all()  # Get all objects initially
      
      if dokumen and dokumen != 'Pilih Dokumen':
         arsip_query = arsip_query.filter(jenis_dokumen_id=dokumen)
      
      if keterangan and keterangan != 'Pilih Keterangan':
         arsip_query = arsip_query.filter(keterangan=keterangan)
      
      # Add additional filters for other parameters as needed
      filtered_arsips = arsip_query.values()
      print(dokumen, keterangan, periode)
      # serializer = FilteredArsipSerializer(filtered_arsips, many=True, context={'request': request})

      # return Response(serializer.data)
      return JsonResponse({'message': 'data berhasil di terima', 'data': list(filtered_arsips)})
   else:
      return JsonResponse({'error': 'gagal'})

def rekap_report(request):
  context  = {
      'data' : '',
      'modul' : 'Laporan Rekap', 
      'links' : {
        'create': 'create-dokumen',
        'delete': 'delete-dokumen',
        'edit': 'edit-dokumen',
      
      }, 
      'parameter': {
        'report' : True,
        'rekap': True
      }
    }

  return render(request, 'report_view.html', context)


def print_detail_report(request):
   context  = {}

   if request.method == 'GET':
         query_set = ArsipModel.objects.all()
         q_object = Q()

         dokumen = request.GET.get('dokumen')
         keterangan = request.GET.get('keterangan')
         periode = request.GET.get('periode_laporan')

         if dokumen and dokumen != 'Pilih Dokumen':
            query_set = ArsipModel.objects.all()
            q_object &= Q(jenis_dokumen=dokumen)
            
         
         if keterangan and keterangan != 'Pilih Keterangan':
            query_set = ArsipModel.objects.all()
            q_object &= Q(keterangan=keterangan)

         if periode: 
            start_date, end_date = periode.split(' - ')
            start_date = datetime.strptime(start_date.strip(), '%m/%d/%Y').date()
            end_date = datetime.strptime(end_date.strip(), '%m/%d/%Y').date()
            q_object &= Q(tanggal_dokumen__range=(start_date, end_date))
         
         query_set = query_set.filter(q_object)
         # Add additional filters for other parameters as needed
         
         print(dokumen, keterangan, periode)
         # Print SQL query
         print(query_set.query)
         
         tanggal_mulai , tanggal_selesai = periode.split('-')
         context['data'] = query_set
         context['dokumen_value'] = dokumen
         context['keterangan_value'] = keterangan
         context['tanggal_mulai'] = tanggal_mulai
         context['tanggal_selesai'] = tanggal_selesai
         
         return render(request, 'report_pdf.html', context)   

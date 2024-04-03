
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponseForbidden
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView 
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
import csv
import json
from .models import PegawaiModel, PegawaiStatusModel
from unit_kerja.models import UnitKerjaModel
from pangkat_golongan.models import PangkatGolonganModel
from .forms import PegawaiForm
from utils.crud_params import CrudParams
from utils.permission import SuperUserRequiredMixin

# Create your views here.

#create paramaters 
pegawaiParams = CrudParams('pegawai')

#LIST VIEW 
# class PegawaiListView(SuperUserRequiredMixin, ListView):
class PegawaiListView(PermissionRequiredMixin, ListView):
  permission_required = 'pegawai.view_pegawaimodel'
  
  model = PegawaiModel
  template_name = 'list_pegawai.html'
  context_object_name = 'data'
  status_pegawai = PegawaiStatusModel.objects.all()
  unit_kerja =  UnitKerjaModel.objects.all()
  extra_context = pegawaiParams.parameter(data_pegawai=True, pegawai=True, status_pegawai=status_pegawai, unit_kerja=unit_kerja, param='Test')

  def handle_no_permission(self):
      return HttpResponseForbidden("You don't have permission to access this page.")

class PegawaiCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'pegawai.add_pegawaimodel'
  form_class = PegawaiForm
  template_name =  'create_pegawai.html'
  extra_context = pegawaiParams.parameter(data_pegawai=True, pegawai=True, action='Buat Data')
  success_url = reverse_lazy('list-pegawai')


class PegawaiUpdate(UpdateView):
  permission_required = 'pegawai.change_pegawaimodel'
  model = PegawaiModel
  form_class = PegawaiForm
  template_name =  'create_pegawai.html'
  # fields = '__all__'
  extra_context = pegawaiParams.parameter(data_pegawai=True, pegawai=True, action='Update Data')
  success_url = reverse_lazy('list-pegawai')


@permission_required('pegawai.delete_pegawaimodel')
def pegawai_delete(req, id):
  pegawai = get_object_or_404(PegawaiModel, id=id)
  pegawai.delete()
  return redirect('list-pegawai')


@permission_required('pegawai.add_pegawaimodel')
def pegawai_import(request):
  if request.method == 'POST' and request.FILES['file_pegawai']:
    status_pegawai = request.POST.get('status_pegawai')
    unit_kerja_pegawai = request.POST.get('unit_kerja')
    csv_file = request.FILES['file_pegawai']
    

    decoded_file=csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(decoded_file)

    for row in csv_reader:
      identitas = row['identitas']
      nama = row['nama']
      jabatan = row['jabatan']
      pangkat_golongan = row['pangkat_golongan']
      
      status = PegawaiStatusModel.objects.get(id=status_pegawai)
      unit_kerja = UnitKerjaModel.objects.get(id=unit_kerja_pegawai)
      pangkat_golongan = PangkatGolonganModel.objects.get(golongan=pangkat_golongan)
      


    # print("STATUS PEGAWAI : ",status_pegawai)
      PegawaiModel.objects.create(identitas=identitas, nama=nama, status=status, jabatan=jabatan, unit_kerja=unit_kerja, pangkat_golongan=pangkat_golongan)

    return redirect('list-pegawai')
  else:
    return redirect('list-pegawai')




@csrf_exempt
# @require_POST
def delete_selected(request):
  
  if request.method == 'POST':
    try:
      #ambil data dari request via json 
      data = json.loads(request.body)

      #seleksi data json 
      seleted_ids = data.get('selected_ids', [])

      #filter data dari data yang dikirim 

      PegawaiModel.objects.filter(id__in=seleted_ids).delete()
      print(seleted_ids)
      return JsonResponse({"message": "data diterima"})
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid JSON data"}, status = 400)

  else:
  
    return JsonResponse({"error": 'Invalid reqeuest'}, status = 400)


def generate_csv(request):
  data = [
    ['identitas', 'nama', 'jabatan', 'pangkat_golongan'],
    ['123123123123', 'Budi', 'Kepala Bidang', 'III/a']
  ]

  # Create csv

  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="template_upload_pegawai.csv"'

   # Create a CSV writer
  writer = csv.writer(response)

    # Write data to CSV
  for row in data:
        # Convert numbers to strings to prevent scientific notation
        row = [str(item) for item in row]
        writer.writerow(row)

  return response
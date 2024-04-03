
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from django.core import paginator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import KlasifikasiModel
from .forms import KlasifikasiForm
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
klasifikasiParams = CrudParams('klasifikasi')

#LIST VIEW 
class KlasifikasiListView(PermissionRequiredMixin, ListView):
  permission_required =  'klasifikasi.view_klasifikasimodel'
  model = KlasifikasiModel
  template_name = 'list_klasifikasi.html'
  context_object_name = 'data'
  extra_context = klasifikasiParams.parameter(data_master=True, klasifikasi=True)
  


class KlasifikasiCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'klasifikasi.create_klasifikasimodel'
  form_class = KlasifikasiForm
  template_name =  'create_klasifikasi.html'
  
  extra_context = klasifikasiParams.parameter(data_master=True, klasifikasi=True, action='Buat Data')
  success_url = reverse_lazy('list-klasifikasi')


class KlasifikasiUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'klasifikasi.change_klasifikasimodel'
  model = KlasifikasiModel
  form_class = KlasifikasiForm
  template_name =  'create_klasifikasi.html'
  extra_context = klasifikasiParams.parameter(data_master=True, klasifikasi=True, action='Update Data')
  success_url = reverse_lazy('list-klasifikasi')


@permission_required('klasifikasi.delete_klasifikasimodel')
def klasifikasi_delete(req, id):
  klasifikasi = get_object_or_404(KlasifikasiModel, id=id)
  klasifikasi.delete()
  return redirect('list-klasifikasi')

@csrf_exempt
@require_POST
def klasifikasi_ajax(request):
   draw = int(request.POST.get('draw', 0))
   start = int(request.POST.get('start', 0))
   length = int(request.POST.get('length', 10))
   search_value = request.POST.get('search[value]', '')
   # Your filtering and sorting logic here
   queryset = KlasifikasiModel.objects.filter(kode_klasifikasi__icontains=search_value)
  #  queryset = KlasifikasiModel.objects.all()

    # Count total records
   total_records = queryset.count()

    # Apply pagination
   queryset = queryset[start:start + length]

    # Prepare data in a format expected by DataTables
   data = [
        {
            'kode_klasifikasi': item.kode_klasifikasi,
            'keterangan': item.keterangan,
            # Add more fields as needed
        }
        for item in queryset
    ]

   response_data = {
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': total_records,
        'data': data,
    }

   return JsonResponse(response_data)






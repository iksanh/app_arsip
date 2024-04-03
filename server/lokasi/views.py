
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .models import LokasiModel
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
lokasiParams = CrudParams('lokasi')

#LIST VIEW 
class LokasiListView(PermissionRequiredMixin, ListView):
  permission_required = 'lokasi.view_lokasimodel'
  model = LokasiModel
  template_name = 'list_lokasi.html'
  context_object_name = 'data'
  extra_context = lokasiParams.parameter(data_master=True, lokasi=True)


class LokasiCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'lokasi.add_lokasimodel'
  model = LokasiModel
  template_name =  'create_lokasi.html'
  fields = '__all__'
  extra_context = lokasiParams.parameter(data_master=True, lokasi=True, action='Buat Data')
  success_url = reverse_lazy('list-lokasi')


class LokasiUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'lokasi.change_lokasimodel'
  model = LokasiModel
  template_name =  'create_lokasi.html'
  fields = '__all__'
  extra_context = lokasiParams.parameter(data_master=True, lokasi=True, action='Update Data')
  success_url = reverse_lazy('list-lokasi')

@permission_required('lokasi.delete_lokasimodel')
def lokasi_delete(req, id):
  lokasi = get_object_or_404(LokasiModel, id=id)
  lokasi.delete()
  return redirect('list-lokasi')




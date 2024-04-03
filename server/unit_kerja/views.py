from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import UnitKerjaModel, SubUnitKerjaModel
from .forms import UnitKerjaForm
from utils.crud_params import CrudParams

#create paramaters 
unitKerjaParams = CrudParams('unit-kerja')

#LIST VIEW 
class UnitKerjaListView(PermissionRequiredMixin, ListView):
  permission_required = 'unit_kerja.view_unitkerjamodel'
  model = UnitKerjaModel
  template_name = 'list_unit_kerja.html'
  context_object_name = 'data'
  extra_context = unitKerjaParams.parameter(data_master=True, unit_kerja=True)


class UnitKerjaCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'unit_kerja.add_unitkerjamodel'
  form_class = UnitKerjaForm
  
  template_name =  'create_unit_kerja.html'
  
  extra_context = unitKerjaParams.parameter(data_master=True, unit_kerja=True, action='Buat Data')
  success_url = reverse_lazy('list-unit-kerja')


class UnitKerjaUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'unit_kerja.change_unitkerjamodel'
  form_class = UnitKerjaForm
  model = UnitKerjaModel
  template_name =  'create_unit_kerja.html'
  
  extra_context = unitKerjaParams.parameter(data_master=True, unit_kerja=True, action='Update Data')
  success_url = reverse_lazy('list-unit-kerja')


@permission_required('unit_kerja.delete_unitkerjamodel')
def unit_kerja_delete(req, id):
  unit_kerja = get_object_or_404(UnitKerjaModel, id=id)
  unit_kerja.delete()
  return redirect('list-unit-kerja')





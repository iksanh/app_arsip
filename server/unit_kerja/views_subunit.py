from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import UnitKerjaModel, SubUnitKerjaModel
from utils.crud_params import CrudParams
from .forms import SubUnitKerjaForm

#create paramaters 
unitKerjaParams = CrudParams('subunit-kerja')

#LIST VIEW 
class SubUnitKerjaListView(PermissionRequiredMixin, ListView):
  permission_required = 'unit_kerja.view_subunitkerjamodel'
  model = SubUnitKerjaModel
  template_name = 'list_subunit_kerja.html'
  context_object_name = 'data'
  extra_context = unitKerjaParams.parameter(data_master=True, subunit_kerja=True)


class SubUnitKerjaCreate(PermissionRequiredMixin,CreateView):
  permission_required = 'unit_kerja.add_subunitkerjamodel'
  form_class = SubUnitKerjaForm
  model = SubUnitKerjaModel
  template_name =  'create_subunit_kerja.html'
  extra_context = unitKerjaParams.parameter(data_master=True, subunit_kerja=True, action='Buat Data')
  success_url = reverse_lazy('list-subunit-kerja')


class SubUnitKerjaUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'unit_kerja.change_subunitkerjamodel'
  model = SubUnitKerjaModel
  form_class = SubUnitKerjaForm
  template_name =  'create_subunit_kerja.html'
  
  extra_context = unitKerjaParams.parameter(data_master=True, subunit_kerja=True, action='Update Data')
  success_url = reverse_lazy('list-subunit-kerja')

@permission_required('unit_kerja.delete_subunitkerjamodel')
def subunit_kerja_delete(req, id):
  unit_kerja = get_object_or_404(SubUnitKerjaModel, id=id)
  unit_kerja.delete()
  return redirect('list-subunit-kerja')





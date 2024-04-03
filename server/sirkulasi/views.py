
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import SirkulasiModel
from .forms import SirkluasiForm
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
sirkulasiParams = CrudParams('sirkulasi')

#LIST VIEW 
class SirkulasiListView(PermissionRequiredMixin, ListView):
  permission_required = 'sirkulasi.view_sirkulasimodel'
  model = SirkulasiModel
  template_name = 'list_sirkulasi.html'
  context_object_name = 'data'
  extra_context = sirkulasiParams.parameter(sirkulasi=True)


class SirkulasiCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'sirkulasi.add_sirkulasimodel'
  model = SirkulasiModel
  form_class = SirkluasiForm
  template_name =  'create_sirkulasi.html'
  
  extra_context = sirkulasiParams.parameter(sirkulasi=True, action='Buat Data')
  success_url = reverse_lazy('list-sirkulasi')

  


class SirkulasiUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'sirkulasi.add_sirkulasimodel'
  model = SirkulasiModel
  template_name =  'create_sirkulasi.html'
  form_class = SirkluasiForm
  # fields = '__all__'
  extra_context = sirkulasiParams.parameter(sirkulasi=True, action='Update Data')
  success_url = reverse_lazy('list-sirkulasi')


@permission_required('sirkulasi.delete_sirkulasimodel')
def sirkulasi_delete(req, id):
  sirkulasi = get_object_or_404(SirkulasiModel, id=id)
  sirkulasi.delete()
  return redirect('list-sirkulasi')




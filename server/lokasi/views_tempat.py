
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .models import TempatModel
from .forms import TempatForm
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
tempatParams = CrudParams('tempat')

#LIST VIEW 
class TempatListView(PermissionRequiredMixin,  ListView):
  permission_required = 'lokasi.view_tempatmodel'
  model = TempatModel
  template_name = 'list_tempat.html'
  context_object_name = 'data'
  extra_context = tempatParams.parameter(data_master=True, tempat=True)


class TempatCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'lokasi.add_tempatmodel'
  form_class = TempatForm
  
  template_name =  'create_tempat.html'
  
  extra_context = tempatParams.parameter(data_master=True, tempat=True, action='Buat Data')
  success_url = reverse_lazy('list-tempat')


class TempatUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'lokasi.change_tempatmodel'
  model = TempatModel
  form_class = TempatForm
  template_name =  'create_tempat.html'
  # fields = '__all__'
  extra_context = tempatParams.parameter(data_master=True, tempat=True, action='Update Data')
  success_url = reverse_lazy('list-tempat')

@permission_required('lokasi.delete_tempatmodel')
def tempat_delete(req, id):
  tempat = get_object_or_404(TempatModel, id=id)
  tempat.delete()
  return redirect('list-tempat')




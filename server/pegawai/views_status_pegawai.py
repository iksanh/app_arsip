
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from .forms import PegawaiForm, PegawaiStatusForm
from .models import PegawaiStatusModel
from utils.crud_params import CrudParams
from utils.permission import SuperUserRequiredMixin, superuser_required


# Create your views here.

#create paramaters 
pegawaiParams = CrudParams('status-pegawai')

#LIST VIEW 
class PegawaiStatusListView(ListView):
  model = PegawaiStatusModel
  template_name = 'list_status_pegawai.html'
  context_object_name = 'data'
  extra_context = pegawaiParams.parameter(data_pegawai=True, status_pegawaii=True)


class PegawaiStatusCreate(SuperUserRequiredMixin, CreateView):
  form_class = PegawaiStatusForm
  
  template_name =  'create_status_pegawai.html'
  
  extra_context = pegawaiParams.parameter(data_pegawai=True, status_pegawaii=True, action='Buat Data')
  success_url = reverse_lazy('list-status-pegawai')


class PegawaiStatusUpdate(SuperUserRequiredMixin, UpdateView):
  model = PegawaiStatusModel
  template_name =  'create_status_pegawai.html'
  form_class= PegawaiStatusForm
  extra_context = pegawaiParams.parameter(data_pegawai=True, status_pegawaii=True, action='Update Data')
  success_url = reverse_lazy('list-status-pegawai')


def pegawai_status_delete(request, id):
  pegawai = get_object_or_404(PegawaiStatusModel, id=id)
  pegawai.delete()
  return redirect('list-status-pegawai')




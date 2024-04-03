from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import PangkatGolonganModel
from .forms import PangkatGolnganForms
from utils.crud_params import CrudParams

# Create your views here.

pangkat_golongan_params = CrudParams('pangkat_golongan')


#LIST VIEW
class PangkatGolonganListView(PermissionRequiredMixin, ListView):
  permission_required = ''
  model = PangkatGolonganModel
  template_name = 'list_pangkat_golongan.html'
  context_object_name = 'data'
  extra_context = pangkat_golongan_params.parameter(data_pegawai=True, pangkat_golongan=True)


class PangkatGolonganCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'klasifikasi.create_klasifikasimodel'
  form_class = PangkatGolnganForms
  template_name =  'pangkat_golongan_form.html'
  extra_context = pangkat_golongan_params.parameter(data_pegawai=True, pangkat_golongan=True, action='Buat Data')
  success_url = reverse_lazy('list-pangkat_golongan')

class PangkatGolonganUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'klasifikasi.change_klasifikasimodel'
  model = PangkatGolonganModel
  form_class = PangkatGolnganForms
  template_name =  'pangkat_golongan_form.html'
  extra_context = pangkat_golongan_params.parameter(pegawai=True, pangkat_golongan=True, action='Buat Data')
  success_url = reverse_lazy('list-pangkat_golongan')

@permission_required('klasifikasi.delete_klasifikasimodel')
def pangkat_golongan_delete(req, id):
  pangkat_golongan = get_object_or_404(PangkatGolonganModel, id=id)
  pangkat_golongan.delete()
  return redirect('list-pangkat_golongan')

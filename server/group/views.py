from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import GroupForm, Group

# Create your views here.

from utils.crud_params import CrudParams

groupParams = CrudParams('group')

class GroupList(PermissionRequiredMixin, ListView):
  permission_required =  'group.view_group'
  model = Group
  template_name = 'auth/list_group.html'
  context_object_name = 'data'
  extra_context = groupParams.parameter(data_pegawai=True, group=True)



class GroupCreate(PermissionRequiredMixin, CreateView):
  permission_required =  'group.create_group'
  form_class = GroupForm
  template_name = 'auth/group_form.html'
  success_url = reverse_lazy('list-group')
  extra_context = groupParams.parameter(data_pegawai=True, group=True)
  

class GroupUpdate(PermissionRequiredMixin, UpdateView):
  permission_required =  'group.change_group'
  model = Group
  form_class = GroupForm
  template_name = 'auth/group_form.html'
  success_url = reverse_lazy('list-group')
  extra_context = groupParams.parameter(data_pegawai=True, group=True)


@permission_required('group.delete_group')
def delete_group(req, id):
  group = get_object_or_404(Group, id=id)
  group.delete()
  return redirect('list-group')
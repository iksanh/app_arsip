
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import MediaModel
from utils.crud_params import CrudParams

# Create your views here.

#create paramaters 
mediaParams = CrudParams('media')

#LIST VIEW 
class MediaListView(PermissionRequiredMixin, ListView):
  permission_required = 'media.view_mediamodel'
  model = MediaModel
  template_name = 'list_media.html'
  context_object_name = 'data'
  extra_context = mediaParams.parameter(data_master=True, media=True)


class MediaCreate(PermissionRequiredMixin, CreateView):
  permission_required = 'media.add_mediamodel'
  model = MediaModel
  template_name =  'create_media.html'
  fields = '__all__'
  extra_context = mediaParams.parameter(data_master=True, media=True, action='Buat Data')
  success_url = reverse_lazy('list-media')


class MediaUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'media.change_mediamodel'
  model = MediaModel
  template_name =  'create_media.html'
  fields = '__all__'
  extra_context = mediaParams.parameter(data_master=True, media=True, action='Update Data')
  success_url = reverse_lazy('list-media')

@permission_required('media.delete_mediamodel')
def media_delete(req, id):
  media = get_object_or_404(MediaModel, id=id)
  media.delete()
  return redirect('list-media')




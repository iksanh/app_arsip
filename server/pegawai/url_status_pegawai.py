from django.urls import path
from .views_status_pegawai import PegawaiStatusListView, PegawaiStatusCreate, PegawaiStatusUpdate, pegawai_status_delete
from utils.permission import SuperUserRequiredMixin


urlpatterns = [
  path('', PegawaiStatusListView.as_view(), name='list-status-pegawai'),
  path('create/', PegawaiStatusCreate.as_view(), name='create-status-pegawai'),
  path('edit/<str:pk>', PegawaiStatusUpdate.as_view(), name='edit-status-pegawai'),
  path('delete/<str:id>', pegawai_status_delete, name='delete-status-pegawai')
]
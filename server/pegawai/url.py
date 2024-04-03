from django.urls import path
from .views import PegawaiListView, PegawaiCreate, PegawaiUpdate, pegawai_delete, pegawai_import, delete_selected, generate_csv


urlpatterns = [
  path('', PegawaiListView.as_view(), name='list-pegawai'),
  path('create/', PegawaiCreate.as_view(), name='create-pegawai'),
  path('edit/<str:pk>', PegawaiUpdate.as_view(), name='edit-pegawai'),
  path('delete/<str:id>', pegawai_delete, name='delete-pegawai'),
  path('import_pegawai/', pegawai_import, name='import-pegawai'),
  path('delete_selected/', delete_selected, name='delete-selected-pegawai'),
  path('download_csv/', generate_csv, name='template-csv-pegawai' )
]
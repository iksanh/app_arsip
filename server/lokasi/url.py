from django.urls import path
from .views import LokasiListView, LokasiCreate, LokasiUpdate, lokasi_delete


urlpatterns = [
  path('', LokasiListView.as_view(), name='list-lokasi'),
  path('create/', LokasiCreate.as_view(), name='create-lokasi'),
  path('edit/<str:pk>', LokasiUpdate.as_view(), name='edit-lokasi'),
  path('delete/<str:id>', lokasi_delete, name='delete-lokasi')
]
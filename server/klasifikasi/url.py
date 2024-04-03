from django.urls import path
from .views import KlasifikasiListView, KlasifikasiCreate, KlasifikasiUpdate, klasifikasi_delete, klasifikasi_ajax


urlpatterns = [
  path('', KlasifikasiListView.as_view(), name='list-klasifikasi'),
  path('ajax/', klasifikasi_ajax, name='ajax-klasifikasi'),
  path('create/', KlasifikasiCreate.as_view(), name='create-klasifikasi'),
  path('edit/<str:pk>', KlasifikasiUpdate.as_view(), name='edit-klasifikasi'),
  path('delete/<str:id>', klasifikasi_delete, name='delete-klasifikasi')
]
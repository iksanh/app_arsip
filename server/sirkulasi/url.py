from django.urls import path
from .views import SirkulasiListView, SirkulasiCreate, SirkulasiUpdate, sirkulasi_delete


urlpatterns = [
  path('', SirkulasiListView.as_view(), name='list-sirkulasi'),
  path('create/', SirkulasiCreate.as_view(), name='create-sirkulasi'),
  path('edit/<str:pk>', SirkulasiUpdate.as_view(), name='edit-sirkulasi'),
  path('delete/<str:id>', sirkulasi_delete, name='delete-sirkulasi')
]
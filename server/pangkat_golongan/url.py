from django.urls import path
from .views import PangkatGolonganCreate, PangkatGolonganListView, PangkatGolonganUpdate, pangkat_golongan_delete


urlpatterns = [
  path('', PangkatGolonganListView.as_view(), name='list-pangkat_golongan'),
  path('create/', PangkatGolonganCreate.as_view(), name='create-pangkat_golongan'),
  path('edit/<str:pk>', PangkatGolonganUpdate.as_view(), name='edit-pangkat_golongan'),
  path('delete/<str:id>', pangkat_golongan_delete, name='delete-pangkat_golongan')
]
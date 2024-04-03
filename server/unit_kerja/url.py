from django.urls import path
from .views import UnitKerjaListView, UnitKerjaCreate, UnitKerjaUpdate, unit_kerja_delete


urlpatterns = [
  path('', UnitKerjaListView.as_view(), name='list-unit-kerja'),
  path('create/', UnitKerjaCreate.as_view(), name='create-unit-kerja'),
  path('edit/<str:pk>', UnitKerjaUpdate.as_view(), name='edit-unit-kerja'),
  path('delete/<str:id>', unit_kerja_delete, name='delete-unit-kerja')
]
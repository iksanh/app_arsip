from django.urls import path
# from .views import SUnitKerjaListView, UnitKerjaCreate, UnitKerjaUpdate, unit_kerja_delete
from .views_subunit import SubUnitKerjaCreate, SubUnitKerjaListView, SubUnitKerjaUpdate , subunit_kerja_delete


urlpatterns = [
  path('', SubUnitKerjaListView.as_view(), name='list-subunit-kerja'),
  path('create/', SubUnitKerjaCreate.as_view(), name='create-subunit-kerja'),
  path('edit/<str:pk>', SubUnitKerjaUpdate.as_view(), name='edit-subunit-kerja'),
  path('delete/<str:id>', subunit_kerja_delete, name='delete-subunit-kerja')
]
from django.urls import path
from .views_tempat import TempatListView, TempatCreate, TempatUpdate, tempat_delete


urlpatterns = [
  path('', TempatListView.as_view(), name='list-tempat'),
  path('create/', TempatCreate.as_view(), name='create-tempat'),
  path('edit/<str:pk>', TempatUpdate.as_view(), name='edit-tempat'),
  path('delete/<str:id>', tempat_delete, name='delete-tempat')
]
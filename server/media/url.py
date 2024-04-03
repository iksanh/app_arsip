from django.urls import path
from .views import MediaListView, MediaCreate, MediaUpdate, media_delete


urlpatterns = [
  path('', MediaListView.as_view(), name='list-media'),
  path('create/', MediaCreate.as_view(), name='create-media'),
  path('edit/<str:pk>', MediaUpdate.as_view(), name='edit-media'),
  path('delete/<str:id>', media_delete, name='delete-media')
]
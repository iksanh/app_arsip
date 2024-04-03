from django.urls import path
from .views import GroupCreate, GroupList, GroupUpdate, delete_group


urlpatterns = [
  path('', GroupList.as_view(), name='list-group'),
  path('create/', GroupCreate.as_view(), name='create-group'),
  path('edit/<str:pk>', GroupUpdate.as_view(), name='edit-group'),
  path('delete/<str:id>', delete_group, name='delete-group')
]
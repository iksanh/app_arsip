from django.urls import path
from .views import UserListView, UserCreate, UserUpdate, UserSettingView, user_delete, create_pegawai_user, reset_pegawai_password


urlpatterns = [
  path('', UserListView.as_view(), name='list-user'),
  path('settings/', UserSettingView.as_view(), name='setting-user'),
  path('reset-password/<str:id>', reset_pegawai_password, name='reset-password'),
  path('create/', UserCreate.as_view(), name='create-user'),
  path('edit/<str:pk>', UserUpdate.as_view(), name='edit-user'),
  path('delete/<str:id>', user_delete, name='delete-user'),
  path('create_pengelola/<str:id>', create_pegawai_user, name='create-pegawai-user')
]
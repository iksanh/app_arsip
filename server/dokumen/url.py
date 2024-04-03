from django.urls import path
from .views import list_dokumen, create_dokumen, edit_dokumen, delete_dokumen


urlpatterns = [
  path('', list_dokumen, name='list-dokumen'),
  path('create/', create_dokumen, name='create-dokumen'),
  path('edit/<str:pk>', edit_dokumen, name='edit-dokumen'),
  path('delete/<str:id>', delete_dokumen, name='delete-dokumen')
]
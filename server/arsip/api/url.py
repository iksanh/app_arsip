from django.urls import  path
from .views import ArsipListApi, ArsipDetailApi, arsip_model_api

urlpatterns =[
    path('', ArsipListApi.as_view(), name='arsip_list'),
    path('keterangan/', arsip_model_api),
    path('<str:pk>/', ArsipDetailApi.as_view(), name='arsip_detail'),
]
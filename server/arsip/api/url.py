from django.urls import  path
from .views import (ArsipListApi, ArsipDetailApi)

urlpatterns =[
    path('', ArsipListApi.as_view(), name='arsip_list'),
    path('<str:pk>', ArsipDetailApi.as_view(), name='arsip_detail'),
]
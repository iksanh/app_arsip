from django.urls import path
from pegawai.api.view import PegawaiListApi, PegawaiDetailApi, PegawaiStatusListApi, PegawaiStatuDetailApi

urlpatterns=[
    path('', PegawaiListApi.as_view(), name='list-pegawai'),
    path('<str:pk>', PegawaiDetailApi.as_view(), name='detail-pegawai'),
    path('status/', PegawaiStatusListApi.as_view(), name='status-pegawai'),
    path('status/<str:pk>', PegawaiStatuDetailApi.as_view(), name='detail-status-pegawai')
]
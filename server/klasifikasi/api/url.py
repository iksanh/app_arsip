from django.urls import path
from .views import KlasifikasiListApi, KlasifikasiDetailApi


urlpatterns =[
    path('', KlasifikasiListApi.as_view()),
    path('<str:pk>', KlasifikasiDetailApi.as_view())
]
from django.urls import path
from .views import LokasiListApi, LokasiDetailApi, TempatListApi, TempatDetailApi


urlpatterns = [
    path('', LokasiListApi.as_view()),
    path('<str:pk>', LokasiDetailApi.as_view()),
    path('tempat/', TempatListApi.as_view()),
    path('tempat/<str:pk>', TempatDetailApi.as_view())
]
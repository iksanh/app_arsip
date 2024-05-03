from django.urls import path
from .view import DokumenListApi, DokumenDetailApi

urlpatterns = [
    path('', DokumenListApi.as_view()),
    path('<str:pk>', DokumenDetailApi.as_view())
]
from django.urls import path
from .view import MediaListApi, MediaDetailApi

urlpatterns = [
    path('', MediaListApi.as_view()),
    path('<str:pk>', MediaDetailApi.as_view())
]
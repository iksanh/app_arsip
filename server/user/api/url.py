from django.urls import path
from .view import UserListApi, UserDetailApi

urlpatterns = [
    path('', UserListApi.as_view(), name='list-user'),
    path('<str:pk>/', UserDetailApi.as_view(), name='detail-user')
]
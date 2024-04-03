from rest_framework import generics
from .serializers import User, UserSerializer

class UserListApi(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

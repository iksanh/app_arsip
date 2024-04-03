from rest_framework import  generics
from .serializers import KlasifikasiSerializer, KlasifikasiModel

class KlasifikasiListApi(generics.ListCreateAPIView):
    serializer_class = KlasifikasiSerializer
    queryset = KlasifikasiModel.objects.all()
    

class KlasifikasiDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KlasifikasiSerializer
    queryset = KlasifikasiModel.objects.all()

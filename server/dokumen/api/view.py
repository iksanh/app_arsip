from rest_framework import generics
from .serializers import DokumenSerializer, dokumen


class DokumenListApi(generics.ListCreateAPIView):
    queryset = dokumen.objects.all()
    serializer_class = DokumenSerializer


class DokumenDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = dokumen.objects.all()
    serializer_class = DokumenSerializer

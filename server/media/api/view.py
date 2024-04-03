from rest_framework import generics
from .serializers import MediaSerializer, media


class MediaListApi(generics.ListCreateAPIView):
    queryset = media.objects.all()
    serializer_class = MediaSerializer


class MediaDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = media.objects.all()
    serializer_class = MediaSerializer

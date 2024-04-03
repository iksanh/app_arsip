from rest_framework import generics,status

from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import SirkulasiSerializer, SirkulasiModel

class SirkulasiListApi(APIView):

    def get(self, request, format=None):
        sirkulasi = SirkulasiModel.objects.all()
        serializer = SirkulasiSerializer(sirkulasi, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SirkulasiSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SirkulasiDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SirkulasiSerializer
    queryset = SirkulasiModel.objects.all()

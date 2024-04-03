from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
from .serializers import PegawaiModel, PegawaiStatusModel, PegawaiSerializer, PegawaiStatusSerializer, PegawaiSerializerList


class PegawaiStatusListApi(generics.ListCreateAPIView):
    serializer_class = PegawaiStatusSerializer
    queryset = PegawaiStatusModel.objects.all()

class PegawaiStatuDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PegawaiStatusSerializer
    queryset = PegawaiStatusModel.objects.all()


class PegawaiListApi(APIView):

    def get(self, request, format=None):
        pegawai = PegawaiModel.objects.all()
        serializer = PegawaiSerializerList(pegawai, many=True)
        # serializer = PegawaiSerializer(pegawai, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PegawaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PegawaiDetailApi(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PegawaiSerializer
    queryset = PegawaiModel.objects.all()




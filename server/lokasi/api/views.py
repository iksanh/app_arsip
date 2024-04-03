from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


from .serializers import LokasiSerializer, LokasiModel, TempatSerializer, TempatSerializerList, TempatModel


class LokasiListApi(generics.ListCreateAPIView):
    queryset = LokasiModel.objects.all()
    serializer_class = LokasiSerializer


class LokasiDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = LokasiModel.objects.all()
    serializer_class = LokasiSerializer



class TempatListApi(APIView):
    """
    LIST SEMUA Tempat, 
    """

    def get(self, request, format=None):
        
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Override default page size if needed
        queryset = TempatModel.objects.all()  # Your queryset
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TempatSerializerList(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request, format=None):
        serialzer = TempatSerializer(data=request.data)   
        
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED) 
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
   


class TempatDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = TempatModel.objects.all()
    serializer_class = TempatSerializer



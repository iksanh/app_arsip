from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializers import (UnitKerjaSerializer, SubUnitKerjaSerializer, SubUnitKerjaSerializerList, UnitKerjaModel, SubUnitKerjaModel)



class UnitKerjaApiList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UnitKerjaSerializer
    queryset = UnitKerjaModel.objects.all()


class UnitKerjaApiDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = UnitKerjaSerializer
    queryset = UnitKerjaModel.objects.all()



class SubUnitKerjaApiList(APIView):
    """LIST SEMUA SUB UNIT KERJA"""
    
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        queryset = SubUnitKerjaModel.objects.all()
        result_page = paginator.paginate_queryset(queryset,request)
        serializer = SubUnitKerjaSerializerList(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubUnitKerjaSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # serializer_class = SubUnitKerjaSerializer
    # queryset = SubUnitKerjaModel.objects.all()


class SubUnitKerjaApiDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubUnitKerjaSerializer
    queryset = SubUnitKerjaModel.objects.all()

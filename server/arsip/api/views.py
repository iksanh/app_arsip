from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .serializers import (ArsipSerializer, ArsipModel, ArsipSerializerList)


# class ArsipListApi(generics.ListCreateAPIView):
#     serializer_class = ArsipSerializer
#     queryset = ArsipModel.objects.all()

class ArsipListApi(APIView):

    def get(self, request,format=None):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        queryset = ArsipModel.objects.all()
        result_page = paginator.paginate_queryset(queryset,request)
        serializer = ArsipSerializerList(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        pass

    def post(self, request,format=None):
        serializer = ArsipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArsipDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArsipSerializer
    queryset = ArsipModel.objects.all()





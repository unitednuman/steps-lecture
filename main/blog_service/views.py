from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Reporter
from .serializers import ReporterSerializers
from rest_framework import generics, response, status


# from rest_framework import generics
# from .models import Reporter
# from .serializers import ReporterSerializer


# Create your views here.
# class ReporterView(generics.ListCreateAPIView):
#     permission_classes = []
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers
# class ReporterViewDetails(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     queryset = Reporter.objects.all()
#     serializer_class = ReporterSerializers


class ReporterView(generics.GenericAPIView):
    permission_classes = []
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers

    def get(self, *args, **kwargs):
        data = self.queryset.all()
        paginated = self.paginate_queryset(data)
        serialized = self.get_serializer(paginated, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serlized = self.get_serializer(data = data)
        if serlized.is_valid():
            serlized.save()
            return response.Response(serlized.data,status=status.HTTP_201_CREATED)
        return response.Response(serlized.eroors, status=status.HTTP_400_BAD_REQUEST)


class ReporterViewDetails(generics.GenericAPIView):
    permission_classes = []
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializers

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                data = self.queryset.get(pk=kwargs.get('pk'))
                serialized = self.get_serializer(data)
                return response.Response(serialized.data)
        except ObjectDoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data)
            return response.Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            data.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UploadSerializer
from .models import *
from django.shortcuts import get_object_or_404
import zipfile

# Create your views here.


class DataUploadViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({'status': 'ok'})

    def create(self, request):
        if request.data['file_type'] == 'zip':
            zip_ref = zipfile.ZipFile(request.data['image'], 'r')
            print zip_ref
            return Response(status.HTTP_201_CREATED)
        else:
            serializer_class = UploadSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(status.HTTP_201_CREATED)
            else:
                return Response({'status': status.HTTP_400_BAD_REQUEST,
                                 'error': serializer_class.errors})

    def update(self, request, pk=None):
        image_upload = get_object_or_404(ImageUpload, id=pk)
        serializer_class = UploadSerializer(image_upload, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(status.HTTP_201_CREATED)
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST,
                             'error': serializer_class.errors})


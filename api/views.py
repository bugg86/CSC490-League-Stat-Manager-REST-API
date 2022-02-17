from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import ItemsSerializer, QueueSerializer
from .models import Items, Queues

class ItemsViewset(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('itemid')
    serializer = ItemsSerializer

class QueueViewset(viewsets.ModelViewSet) :
    queryset = Queues.objects().all().order_by('queueid')
    serializer = QueueSerializer
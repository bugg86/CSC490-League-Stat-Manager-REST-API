from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import ItemsSerializer, QueueSerializer, RuneSerializer, RuneStyleSerializer, LeagueSerializer, MapSerializer, ChampionSerializer, ChampionMasterySerializer
from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery

class ItemsViewset(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('itemid')
    serializer_class = ItemsSerializer

class QueueViewset(viewsets.ModelViewSet) :
    queryset = Queues.objects.all().order_by('queueid')
    serializer_class = QueueSerializer

class RuneViewset(viewsets.ModelViewSet) :
    queryset = Runes.objects.all().order_by('runeid')
    serializer_class = RuneSerializer

class RunestyleViewset(viewsets.ModelViewSet) :
    queryset = Runestyles.objects.all().order_by('styleid')
    serializer_class = RuneStyleSerializer

class LeagueViewset(viewsets.ModelViewSet) :
    queryset = Leagues.objects.all().order_by('leagueid')
    serializer_class = LeagueSerializer

class MapViewset(viewsets.ModelViewSet) :
    queryset = Maps.objects.all().order_by('mapid')
    serializer_class = MapSerializer

class ChampionViewset(viewsets.ModelViewSet) :
    queryset = Champions.objects.all().order_by('championid')
    serializer_class = ChampionSerializer

class ChampionMasteryViewset(viewsets.ModelViewSet) :
    queryset = Championmastery.objects.all().order_by('summonerid')
    serializer_class = ChampionMasterySerializer
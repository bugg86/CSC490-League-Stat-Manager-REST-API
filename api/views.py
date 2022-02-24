from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ItemsSerializer, QueueSerializer, RuneSerializer, RuneStyleSerializer, LeagueSerializer, MapSerializer, ChampionSerializer, ChampionMasterySerializer, SummonerSpellSerializer, SummonerSerializer
from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners

class ItemsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = Items.objects.all().order_by('itemid')
    serializer_class = ItemsSerializer

class QueueViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Queues.objects.all().order_by('queueid')
    serializer_class = QueueSerializer

class RuneViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Runes.objects.all().order_by('runeid')
    serializer_class = RuneSerializer

class RunestyleViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Runestyles.objects.all().order_by('styleid')
    serializer_class = RuneStyleSerializer

class LeagueViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Leagues.objects.all().order_by('leagueid')
    serializer_class = LeagueSerializer

class MapViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Maps.objects.all().order_by('mapid')
    serializer_class = MapSerializer

class ChampionViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Champions.objects.all().order_by('championid')
    serializer_class = ChampionSerializer

class ChampionMasteryViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Championmastery.objects.all().order_by('summonerid')
    serializer_class = ChampionMasterySerializer

class SummonerSpellViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Summonerspells.objects.all().order_by('spellkey')
    serializer_class = SummonerSpellSerializer

class SummonerViewset(viewsets.ModelViewSet) :
    permissions_classes = (IsAuthenticated,)
    queryset = Summoners.objects.all().order_by('id')
    serializer_class = SummonerSerializer
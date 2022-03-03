from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ItemsSerializer, QueueSerializer, RuneSerializer, RuneStyleSerializer, LeagueSerializer, MapSerializer, ChampionSerializer, ChampionMasterySerializer, SummonerSpellSerializer, SummonerSerializer, MatchSerializer, MatchParticipantSerializer, MatchteamSerializer
from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners, Matches, Matchparticipants, Matchteams

class ItemsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = Items.objects.all().order_by('itemid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'itemid', 
        'name', 
        'cost_base', 
        'cost_purchaseable', 
        'cost_total', 
        'cost_sell', 
        'isrune', 
        'description', 
        'colloq', 
        'plaintext', 
        'consumed', 
        'stacks', 
        'depth', 
        'consumeonfull', 
        '_from', 
        '_into', 
        'specialrecipe', 
        'instore', 
        'hidefromall', 
        'requiredchampion', 
        'requireddaily', 
        'flathppoolmod', 
        'flatmppoolmod', 
        'flathpregenmod', 
        'flatmpregenmod', 
        'flatarmormod', 
        'flatphysicaldamagemod', 
        'flatmagicdamagemod', 
        'flatmovementspeedmod', 
        'percentmovementspeedmod', 
        'percentattackspeedmod', 
        'flatcritchancemod', 
        'flatspellblockmod', 
        'percentlifestealmod', 
        'tags', 
        'map1', 
        'map2', 
        'map3', 
        'map4',
        'effects'
    ]
    serializer_class = ItemsSerializer

class QueueViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Queues.objects.all().order_by('queueid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'queueid', 
        'map', 
        'description'
    ]
    serializer_class = QueueSerializer

class RuneViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Runes.objects.all().order_by('runeid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'runeid', 
        'name', 
        'style', 
        'shortdescription', 
        'longdescription'
    ]
    serializer_class = RuneSerializer

class RunestyleViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Runestyles.objects.all().order_by('styleid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'styleid', 
        'name'
    ]
    serializer_class = RuneStyleSerializer

class LeagueViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Leagues.objects.all().order_by('leagueid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'leagueid', 
        'queuetype', 
        'tier', 
        'rank', 
        'summonerid', 
        'summonername', 
        'leaguepoints', 
        'wins', 
        'losses', 
        'veteran', 
        'inactive', 
        'freshblood', 
        'hotstreak'
    ]
    serializer_class = LeagueSerializer

class MapViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Maps.objects.all().order_by('mapid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'mapid', 
        'mapname'
    ]
    serializer_class = MapSerializer

class ChampionViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Champions.objects.all().order_by('championid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'championid', 
        'name', 
        'version', 
        'title', 
        'blurb', 
        'info_attack', 
        'info_defense', 
        'info_magic', 
        'info_difficulty', 
        'tag1', 
        'tag2', 
        'partype', 
        'stats_hp', 
        'stats_hpperlevel', 
        'stats_mp', 
        'stats_mpperlevel', 
        'stats_movespeed', 
        'stats_armor', 
        'stats_armorperlevel', 
        'stats_spellblock', 
        'stats_spellblockperlevel', 
        'stats_attackrange', 
        'stats_hpregen', 
        'stats_hpregenperlevel', 
        'stats_mpregen', 
        'stats_mpregenperlevel', 
        'stats_crit', 
        'stats_critperlevel', 
        'stats_attackdamage', 
        'stats_attackdamageperlevel', 
        'stats_attackspeedperlevel', 
        'stats_attackspeed'
    ]
    serializer_class = ChampionSerializer

class ChampionMasteryViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Championmastery.objects.all().order_by('summonerid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'summonerid', 
        'championid', 
        'championlevel', 
        'championpoints', 
        'championpointsuntilnextlevel', 
        'chestgranted', 
        'tokensearned'
    ]
    serializer_class = ChampionMasterySerializer

class SummonerSpellViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Summonerspells.objects.all().order_by('spellkey')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'spellkey', 
        'spellid', 
        'name', 
        'cooldown', 
        'description'
    ]
    serializer_class = SummonerSpellSerializer

class SummonerViewset(viewsets.ModelViewSet) :
    permissions_classes = (IsAuthenticated,)
    queryset = Summoners.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        'puuid', 
        'id', 
        'name', 
        'accountid', 
        'summonerlevel', 
        'profileiconid', 
        'revisiondate'
    ]
    serializer_class = SummonerSerializer

class MatchViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Matches.objects.all().order_by('matchid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'matchid', 
        'gamemode', 
        'gameduration', 
        'gamename', 
        'gametype', 
        'mapid', 
        'queueid', 
        'platformid', 
        'gameversion',
        'gamecreation',
        'gameendtimestamp',
        'gamestarttimestamp'
    ]
    serializer_class = MatchSerializer

class MatchparticipantViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Matchparticipants.objects.all().order_by('matchid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'matchid',
        'summonerid',
        'assists',
        'baronkills',
        'bountylevel',
        'champexperience',
        'champlevel',
        'championid',
        'championname',
        'damagedealttobuildings',
        'damagedealttoobjectives',
        'damagedealttoturrets',
        'damageselfmitigated',
        'deaths',
        'detectorwardsplaced',
        'doublekills',
        'dragonkills',
        'firstbloodassist',
        'firstbloodkill',
        'firsttowerassist',
        'firsttowerkill',
        'gameendedinearlysurrender',
        'gameendedinsurrender',
        'goldearned',
        'goldspent',
        'individualpostition',
        'inhibitorkills',
        'inhibitortakedowns',
        'inhibitorslost',
        'item0',
        'item1',
        'item2',
        'item3',
        'item4',
        'item5',
        'item6',
        'itemspurchased',
        'killingsprees',
        'kills',
        'lane', 
        'largestcriticalstrike',
        'largestkillingspree',
        'largestmultikill',
        'longesttimespentliving',
        'magicdamagedealt',
        'magicdamagedealttochampions',
        'magicdamagetaken',
        'neutralminionskilled',
        'nexuskills',
        'nexuslost',
        'nexustakedowns',
        'objectivesstolen',
        'objectivesstolenassists',
        'participantid',
        'pentakills',
        'physicaldamagedealt',
        'physicaldamagedealttochampions',
        'physicaldamagetaken',
        'profileicon',
        'puuid',
        'quadrakills',
        'riotidname',
        'riotidtagline',
        'role',
        'rune1id',
        'rune2id',
        'rune3id',
        'rune4id',
        'rune5id',
        'rune6id',
        'rune7id',
        'runestyle1id',
        'runestyle2id',
        'sightwardsboughtingame',
        'spell1casts',
        'spell2casts',
        'spell3casts',
        'spell4casts',
        'summoner1casts',
        'summoner1id',
        'summoner2casts',
        'summoner2id',
        'summonerlevel',
        'summonername',
        'teamearlysurrendered',
        'teamid',
        'teamposition',
        'timeccingothers',
        'timeplayed',
        'totaldamagedealt',
        'totaldamagedealttochampions',
        'totaldamageshieldedonteammates',
        'totaldamagetaken',
        'totalheal',
        'totalhealsonteammates',
        'totalminionskilled',
        'totaltimeccdealt',
        'totaltimespentdead',
        'totalunitshealed',
        'triplekills',
        'truedamagedealt',
        'truedamagedealttochampions',
        'truedamagetaken',
        'turretkills',
        'turrettakedowns',
        'turretslost',
        'unrealkills',
        'visionscore',
        'visionwardsboughtingame',
        'wardskilled',
        'wardsplaced',
        'win'
    ]
    serializer_class = MatchParticipantSerializer

class MatchteamViewset(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,) 
    queryset = Matchteams.objects.all().order_by('matchid')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'matchid',
        'teamid',
        'win',
        'ban1',
        'ban2',
        'ban3',
        'ban4',
        'ban5',
        'firstbaron',
        'baronkills',
        'firstchampion',
        'championkills',
        'firstdragon',
        'dragonkills',
        'firstinhibitor',
        'inhibitorkills',
        'firstriftherald',
        'riftheraldkills',
        'firsttower',
        'towerkills'
    ]
    serializer_class = MatchteamSerializer
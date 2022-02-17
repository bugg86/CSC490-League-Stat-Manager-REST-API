from .models import Items, Queues, Runes, Runestyles, Leagues, Maps
from rest_framework import serializers

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('itemid', 'name', 'cost', 'sellprice', 'purchaseable')

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queues
        fields = ('queueid', 'map', 'description')

class RuneSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runes
        fields = ('runeid', 'name', 'style', 'row')

class RuneStyleSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runestyles
        fields = ('styleid', 'name')

class LeagueSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Leagues
        fields = ('leagueid', 'queuetype', 'tier', 'rank', 'summonerid', 'summonername', 'leaguepoints', 'wins', 'losses', 'veteran', 'inactive', 'freshblood', 'hotstreak')

class MapSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Maps
        fields = ('mapid', 'mapname')
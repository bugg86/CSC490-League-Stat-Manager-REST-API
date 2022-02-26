from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners, Matches
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

class ChampionSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Champions
        fields = ('championid', 'name')

class ChampionMasterySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Championmastery
        fields = ('summonerid', 'championid', 'championlevel', 'championpoints', 'championpointsuntilnextlevel', 'chestgranted', 'tokensearned')

class SummonerSpellSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summonerspells
        fields = ('spellkey', 'spellid', 'name', 'cooldown')

class SummonerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summoners
        fields = ('id', 'accountid', 'puuid', 'name', 'profileiconid', 'revisiondate', 'summonerlevel')

class MatchSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Matches
        fields = ('matchid', 'gamemode', 'gameduration', 'gamename', 'gametype', 'mapid', 'queueid', 'platformid', 'gameVersion')
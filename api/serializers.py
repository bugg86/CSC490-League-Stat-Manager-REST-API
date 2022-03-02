from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners, Matches
from rest_framework import serializers

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('itemid', 
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
            'from_', 
            'into_', 
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
        )

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queues
        fields = (
            'queueid', 
            'map', 
            'description'
        )

class RuneSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runes
        fields = (
            'runeid', 
            'name', 
            'style', 
            'shortdescription', 
            'longdescription'
        )

class RuneStyleSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runestyles
        fields = (
            'styleid', 
            'name'
        )

class LeagueSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Leagues
        fields = (
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
        )

class MapSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Maps
        fields = (
            'mapid', 
            'mapname'
        )

class ChampionSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Champions
        fields = (
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
        )

class ChampionMasterySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Championmastery
        fields = (
            'summonerid', 
            'championid', 
            'championlevel', 
            'championpoints', 
            'championpointsuntilnextlevel', 
            'chestgranted', 
            'tokensearned'
        )

class SummonerSpellSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summonerspells
        fields = (
            'spellkey', 
            'spellid', 
            'name',
            'cooldown',
            'description'
        )

class SummonerSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summoners
        fields = (
            'id', 
            'accountid', 
            'puuid', 
            'name', 
            'profileiconid', 
            'revisiondate', 
            'summonerlevel'
        )

class MatchSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Matches
        fields = (
            'matchid', 
            'gamemode', 
            'gameduration', 
            'gamename', 
            'gametype', 
            'mapid', 
            'queueid', 
            'platformid', 
            'gameversion'
        )
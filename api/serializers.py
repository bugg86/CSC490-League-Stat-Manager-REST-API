from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners, Matches, Matchparticipants, Matchteams
from rest_framework import serializers

#comment
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queues
        fields = '__all__'

class RuneSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runes
        fields = '__all__'

class RuneStyleSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Runestyles
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Leagues
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Maps
        fields = '__all__'

class ChampionSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Champions
        fields = '__all__'

class ChampionMasterySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Championmastery
        fields = '__all__'

class SummonerSpellSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Summonerspells
        fields = '__all__'

class SummonerSerializer(serializers.ModelSerializer) :
    puuid = serializers.CharField(max_length=100)
    
    class Meta :
        model = Summoners
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Matches
        fields = '__all__'

class MatchParticipantSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Matchparticipants
        fields = '__all__'

class MatchteamSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Matchteams
        fields = '__all__'
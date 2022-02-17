from .models import Items, Queues
from rest_framework import serializers

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('itemid', 'name', 'cost', 'sellprice', 'purchaseable')

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('queueid', 'map', 'description')
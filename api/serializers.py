from .models import Items
from rest_framework import serializers

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('itemid', 'name', 'cost', 'sellprice', 'purchaseable')
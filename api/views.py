from rest_framework import viewsets

from .serializers import ItemsSerializer
from .models import Items

class ItemsViewset(viewsets.ModelViewSet) :
    queryset = Items.objects.all().order_by('itemid')
    serializer_class = ItemsSerializer
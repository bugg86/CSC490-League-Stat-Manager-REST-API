from django.urls import include, path
from rest_framework import routers

from .views import ItemsViewset, QueueViewset, RuneViewset, RunestyleViewset

router = routers.DefaultRouter()
router.register(r'items', ItemsViewset)
router.register(r'queues', QueueViewset)
router.register(r'runes', RuneViewset)
router.register(r'runestyles', RunestyleViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
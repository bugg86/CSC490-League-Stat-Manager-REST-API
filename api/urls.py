from django.urls import include, path
from rest_framework import routers

from .views import ItemsViewset, QueueViewset, RuneViewset, RunestyleViewset, LeagueViewset, MapViewset, ChampionViewset, ChampionMasteryViewset, SummonerSpellViewset, SummonerViewset, MatchViewset, MatchparticipantViewset

router = routers.DefaultRouter()
router.register(r'items', ItemsViewset)
router.register(r'queues', QueueViewset)
router.register(r'runes', RuneViewset)
router.register(r'runestyles', RunestyleViewset)
router.register(r'leagues', LeagueViewset)
router.register(r'maps', MapViewset)
router.register(r'champions', ChampionViewset)
router.register(r'championmasteries', ChampionMasteryViewset)
router.register(r'summonerspells', SummonerSpellViewset)
router.register(r'summoners', SummonerViewset)
router.register(r'matches', MatchViewset)
router.register(r'matchparticipants', MatchparticipantViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
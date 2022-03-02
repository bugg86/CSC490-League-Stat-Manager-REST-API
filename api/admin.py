from django.contrib import admin
from .models import Items, Queues, Runes, Runestyles, Leagues, Maps, Champions, Championmastery, Summonerspells, Summoners, Matches, Matchparticipants

# Register your models here.

admin.site.register(Items)
admin.site.register(Queues)
admin.site.register(Runes)
admin.site.register(Runestyles)
admin.site.register(Leagues)
admin.site.register(Maps)
admin.site.register(Champions)
admin.site.register(Championmastery)
admin.site.register(Summonerspells)
admin.site.register(Summoners)
admin.site.register(Matches)
admin.site.register(Matchparticipants)
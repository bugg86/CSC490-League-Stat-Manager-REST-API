from django.contrib import admin
from .models import Items, Queues, Runes, Runestyles, Leagues

# Register your models here.

admin.site.register(Items)
admin.site.register(Queues)
admin.site.register(Runes)
admin.site.register(Runestyles)
admin.site.register(Leagues)
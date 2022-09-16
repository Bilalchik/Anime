from django.contrib import admin

from .models import Studio, Genre, Anime, Season, Episode

admin.site.register(Studio)
admin.site.register(Genre)
admin.site.register(Anime)
admin.site.register(Season)
admin.site.register(Episode)

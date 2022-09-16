from django.shortcuts import render

from .models import Anime


def index(request):

    all_anime = Anime.objects.all()

    context = {
        'trending_now': all_anime,
        'popular_shows': all_anime,
        'recently_added_shows': all_anime
    }

    return render(request, template_name='app/index.html', context=context)

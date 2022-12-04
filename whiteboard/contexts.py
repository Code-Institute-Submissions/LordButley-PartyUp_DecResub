from .models import Game


def extra_context(request):
    """
    Provides global access to some model
    """

    games = Game.objects.values_list('title', 'ref_name')

    context = {
        'nav_games': games,
    }

    return context

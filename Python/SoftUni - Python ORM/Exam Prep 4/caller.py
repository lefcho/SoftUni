import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import TennisPlayer, Tournament, Match


def get_tennis_players(search_name=None, search_country=None) -> str:
    if search_name is None and search_country is None:
        return ''

    name_query = Q(full_name__icontains=search_name)
    country_query = Q(country__icontains=search_country)

    if search_name is not None and search_country is not None:
        query = Q(name_query & country_query)
    elif search_name is not None:
        query = name_query
    else:
        query = country_query

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players:
        return ''

    return '\n'.join(f'Tennis Player: {p.full_name}, country: {p.country}, '
                     f'ranking: {p.ranking}' for p in players)


def get_top_tennis_player():
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if top_player is None:
        return ''

    return f'Top Tennis Player: {top_player.full_name} with {top_player.win_count} wins.'


def get_tennis_player_by_matches_count():
    top_player = (TennisPlayer.objects
                  .annotate(matches_played=Count('matches'))
                  .order_by('-matches_played', 'ranking')
                  .first()
    )

    if top_player is None or not top_player.matches_played:
        return ''

    return f'Tennis Player: {top_player.full_name} with {top_player.matches_played} matches played.'


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''

    tournaments = (Tournament.objects
                   .annotate(matches_played=Count('matches'))
                   .filter(surface_type__icontains=surface)
                   .order_by('-start_date')
    )

    if not tournaments:
        return ''

    return '\n'.join(f'Tournament: {t.name}, start date: {t.start_date}, matches: '
                     f'{t.matches_played}' for t in tournaments)


def get_latest_match_info():
    latest_match = (Match.objects
                    .prefetch_related('players')
                    .order_by('-date_played', '-id')
                    .first()
    )

    if latest_match is None:
        return ''

    latest_players = latest_match.players.order_by('full_name')
    player_one = latest_players[0].full_name
    player_two = latest_players[1].full_name
    winner = 'TBA' if latest_match.winner is None else latest_match.winner.full_name

    return (f'Latest match played on: {latest_match.date_played}, tournament: {latest_match.tournament.name}, '
            f'score: {latest_match.score}, players: {player_one} vs {player_two}, '
            f'winner: {winner}, summary: {latest_match.summary}')


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return 'No matches found.'

    matches = (Match.objects.select_related('winner')
               .filter(tournament__name__exact=tournament_name)
               .order_by('-date_played'))

    if not matches:
        return 'No matches found.'

    return '\n'.join(
        f'Match played on: {m.date_played}, score: {m.score}, '
        f'winner: {"TBA" if not m.winner else m.winner.full_name}'
        for m in matches
    )





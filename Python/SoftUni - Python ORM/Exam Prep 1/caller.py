import os
import django
from django.db.models import Q, F, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Movie, Actor, Director


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    search_by_name = Q(full_name__icontains=search_name)
    search_by_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(search_by_name & search_by_nationality)
    elif search_name is not None:
        query = search_by_name
    else:
        query = search_by_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ''

    return '\n'.join(f'Director: {d.full_name}, nationality:'
                     f' {d.nationality}, experience: {d.years_of_experience}' for d in directors)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    if not top_director:
        return ''

    return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."


def get_top_actor():
    top_actor = Actor.objects.prefetch_related('starred_movies') \
        .annotate(movies_count=Count('starred_movies'),
                  avg_ratind=Avg('starred_movies__rating')) \
        .order_by('-movies_count', 'full_name') \
        .first()

    if not top_actor or not top_actor.movies_count:
        return ''

    movies = ', '.join(m.title for m in top_actor.starred_movies.all() if m)

    return (f"Top Actor: {top_actor.full_name}, starring in movies: {movies},"
            f" movies average rating: {top_actor.avg_ratind:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('movies') \
                 .annotate(movies_count=Count('movies')) \
                 .order_by('-movies_count', 'full_name')[:3]

    if not actors or not actors[0].movies_count:
        return ''

    return '\n'.join(f'{a.full_name}, participated in {a.movies_count} movies' for a in actors)


def get_top_rated_awarded_movie():
    top_movie = (Movie.objects.select_related('starring_actor')
                 .prefetch_related('actors')
                 .filter(is_awarded=True)
                 .order_by('-rating', 'title')
                 .first())

    if not top_movie:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'

    participating_actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)

    cast = ', '.join(participating_actors)

    return (f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating}."
            f" Starring actor: {starring_actor}. Cast: {cast}.")


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lte=9.9)

    if not movies_to_update:
        return 'No ratings increased.'

    updated_movies_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)
    return f'Rating increased for {updated_movies_count} movies.'






















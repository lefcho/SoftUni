import os
import django
from django.db.models import Q, Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    astronauts = (Astronaut.objects
                  .filter(Q(name__icontains=search_string) | Q(phone_number__icontains=search_string))
                  .order_by('name'))

    if not astronauts:
        return ''

    return '\n'.join(f'Astronaut: {a.name}, phone number: {a.phone_number}'
                     f', status: {"Active" if a.is_active else "'Inactive'"}' for a in astronauts)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if top_astronaut is None or top_astronaut.mission_count == 0:
        return 'No data.'

    return f'Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_count} missions.'


def get_top_commander():
    top_commander = (Astronaut.objects.annotate(mission_count=Count('commander_missions'))
                     .order_by('-mission_count', 'phone_number')).first()

    if top_commander is None or top_commander.mission_count == 0:
        return 'No data.'

    return f'Top Commander: {top_commander.name} with {top_commander.mission_count} commanded missions.'














import os
import django
from django.db.models import Q, Count, F, Avg, Sum

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Mission, Spacecraft


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    astronauts = (Astronaut.objects
                  .filter(Q(name__icontains=search_string) | Q(phone_number__icontains=search_string))
                  .order_by('name'))

    if not astronauts:
        return ''

    return '\n'.join(f'Astronaut: {a.name}, phone number: {a.phone_number}'
                     f', status: {"Active" if a.is_active else "Inactive"}' for a in astronauts)


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


def get_last_completed_mission():
    last_mission = (Mission.objects
                    .annotate(total_spacewalks=Sum('astronauts__spacewalks'))
                    .filter(status='Completed')
                    .order_by('-launch_date')
                    .select_related('commander', 'spacecraft')
                    .prefetch_related('astronauts')
                    .first())

    if last_mission is None:
        return 'No data.'

    commander_name = last_mission.commander.name if last_mission.commander else 'TBA'
    astronauts = last_mission.astronauts.order_by('name')
    astronaut_names = ', '.join(astronaut.name for astronaut in astronauts)

    return (f"The last completed mission is: {last_mission.name}. Commander: {commander_name}."
            f" Astronauts: {astronaut_names}. Spacecraft: {last_mission.spacecraft.name}."
            f" Total spacewalks: {last_mission.total_spacewalks}.")


def get_most_used_spacecraft():
    top_spacecraft = (Spacecraft.objects
                      .annotate(mission_count=Count('missions'))
                      .order_by('-mission_count', 'name')
                      .first())

    if top_spacecraft is None or top_spacecraft.mission_count == 0:
        return 'No data.'

    astronauts = set()
    for mission in top_spacecraft.missions.all():
        astronauts.update(mission.astronauts.values_list('id', flat=True))
    num_astronauts = len(astronauts)

    return (f'The most used spacecraft is: {top_spacecraft.name}, manufactured by {top_spacecraft.manufacturer}, '
            f'used in {top_spacecraft.mission_count} missions, astronauts on missions: {num_astronauts}.')


def decrease_spacecrafts_weight():
    planned_spacecraft_ids = (Mission.objects
                              .filter(status='Planned')
                              .values_list('spacecraft_id', flat=True)
                              .distinct())

    spacecrafts_updated = (Spacecraft.objects
                           .filter(id__in=planned_spacecraft_ids, weight__gte=200.0)
                           .update(weight=F('weight') - 200.0))

    if not spacecrafts_updated:
        return 'No changes in weight.'

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f'The weight of {spacecrafts_updated} spacecrafts has been decreased. '
            f'The new average weight of all spacecrafts is {avg_weight:.1f}kg')

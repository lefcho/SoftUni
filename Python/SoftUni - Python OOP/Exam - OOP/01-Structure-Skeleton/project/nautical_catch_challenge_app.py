from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    @staticmethod
    def check_health(diver: BaseDiver):
        if diver.oxygen_level <= 0:
            diver.has_health_issue = True

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in ['ScubaDiver', 'FreeDiver']:
            return f"{diver_type} is not allowed in our competition."

        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        if diver_type == 'FreeDiver':
            new_diver = FreeDiver(diver_name)
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."
        new_diver = ScubaDiver(diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in ['PredatoryFish', 'DeepSeaFish']:
            return f"{fish_type} is forbidden for chasing in our competition."

        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        if fish_type == 'PredatoryFish':
            new_fish = PredatoryFish(fish_name, points)
            self.fish_list.append(new_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."
        new_fish = DeepSeaFish(fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver_found = False
        fish_found = False
        for diver in self.divers:
            if diver.name == diver_name:
                competing_diver = diver
                diver_found = True
                break
        if not diver_found:
            return f"{diver_name} is not registered for the competition."

        for fish in self.fish_list:
            if fish.name == fish_name:
                fish_to_catch = fish
                fish_found = True
                break
        if not fish_found:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if competing_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if competing_diver.oxygen_level < fish_to_catch.time_to_catch:
            competing_diver.miss(fish_to_catch.time_to_catch)
            self.check_health(competing_diver)
            return f"{diver_name} missed a good {fish_name}."
        elif competing_diver.oxygen_level == fish_to_catch.time_to_catch:
            if is_lucky:
                competing_diver.hit(fish_to_catch)
                self.check_health(competing_diver)
                return f"{diver_name} hits a {fish_to_catch.points}pt. {fish_name}."
            competing_diver.miss(fish_to_catch.time_to_catch)
            self.check_health(competing_diver)
            return f"{diver_name} missed a good {fish_name}."
        else:
            competing_diver.hit(fish_to_catch)
            self.check_health(competing_diver)
            return f"{diver_name} hits a {fish_to_catch.points}pt. {fish_name}."

    def health_recovery(self):
        counter = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                counter += 1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        for diver in self.divers:
            if diver.name == diver_name:
                current_diver = diver
                break

        result = f'**{diver_name} Catch Report**\n'
        result += '\n'.join([f.fish_details() for f in current_diver.catch])
        return result

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        statistics = "**Nautical Catch Challenge Statistics**\n"
        statistics += '\n'.join([str(d) for d in sorted_divers])

        return statistics

def team_lineup(*args):
    result = ''
    country_players_dict= {}
    for player, country in args:
        if country not in country_players_dict:
            country_players_dict[country] = []
        country_players_dict[country].append(player)

    country_players_dict = dict(sorted(country_players_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    for country, players in country_players_dict.items():
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
print()
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print()
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))



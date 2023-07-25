team_A = []
team_B = []
team_A_players = 11
team_B_players = 11
is_terminated = False
player_list = input().split()

for player in player_list:
    if player in team_A or player in team_B:
        continue
    if "A-" in player:
        team_A.append(player)
        team_A_players -= 1
        if team_A_players < 7:
            is_terminated = True
            break
    elif "B-" in player:
        team_B.append(player)
        team_B_players -= 1
        if team_B_players < 7:
            is_terminated = True
            break

print(f"Team A - {team_A_players}; Team B - {team_B_players}")

if is_terminated:
    print("Game was terminated")
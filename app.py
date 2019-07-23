#!/usr/bin/env python3

import constants
from math import ceil

def clean_data():
    # calculate players per team
    per_team = ceil(len(constants.PLAYERS) / len(constants.TEAMS))
    teams = []

    # init ranges for equally splitting players to teams
    start = 0
    stop = per_team
    for t_idx, team in enumerate(constants.TEAMS):
        players = constants.PLAYERS[start:stop]

        for player in players:
            # clean up height and experience data
            name, guardians, experience, height = player.values()
            player['height'] = int(height[:2])
            player['experience'] = True if experience == 'YES' else False

        # add new team with players
        teams.append({'team': team, 'players': players})

        # update ranges
        start += per_team
        stop = start+per_team

    return teams

def main_menu():
    choices = ['display team stats', 'quit']
    print('---- MENU ----\n\n  Here are your choices:')
    for i, c in enumerate(choices,1): print(f'   {i}) {c.title()}')
    # return len of choices; 'quit' is always at the end
    return len(choices)

def stats_menu(teams):
    team_names = [t['team'] for t in teams]
    for i, t in enumerate(team_names, 1): print(f'{i}) {t}')

def show_stats(teams, idx):
    # get selected team
    team, players = teams[idx].values()
    header = f'Team: {team} Stats'
    # collect player names
    player_names = [p['name'] for p in players]

    print(header)
    print('-'*len(header))
    print(f'Total players: {len(player_names)}')
    print(f'Players: \n\t{", ".join(player_names)}')

def prompt():
    res = int(input('\n\nEnter an option > '))
    print('\n')
    return res
    
def cont():
    input('\n\nPress ENTER to continue...\n\n')

if __name__ == '__main__':
    teams = clean_data()
    main_choice = 0

    while main_choice != main_menu():
        main_choice = prompt()

        if main_choice == 1:
            stats_menu(teams)
            team_choice = prompt()
            show_stats(teams, team_choice-1)
            cont() 

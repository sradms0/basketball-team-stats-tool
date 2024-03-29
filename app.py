#!/usr/bin/env python3

import constants
from os import system, name
from math import ceil

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def clean_data():
    # calculate players per team
    per_team = ceil(len(constants.PLAYERS) / len(constants.TEAMS))
    experienced = 0
    inexperienced = 0
    teams = []

    # init ranges for equally splitting players to teams
    start = 0
    stop = per_team
    for t_idx, team in enumerate(constants.TEAMS):
        players = constants.PLAYERS[start:stop]

        data = {'team': team, 'players': None, 'experienced': 0, 'inexperienced': 0}
        for player in players:
            # clean up experience, guardians, and height data
            name, guardians, experience, height = player.values()
            experience = True if experience == 'YES' else False

            player['experience'] = experience
            player['guardians'] = guardians.split(' and ')
            player['height'] = int(height[:2])

            if experience: data['experienced'] += 1
            else: data['inexperienced'] += 1

        # add new team with players
        data['players'] = players
        teams.append(data)

        # update ranges
        start += per_team
        stop = start+per_team

    return teams

def show_all_teams(teams):
    for i, t in enumerate(teams): show_stats(teams, i)

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
    team, players, experienced, inexperienced = teams[idx].values()
    player_names = []
    guardian_names = []
    total_height = 0

    # collect/calculate data to display
    for p in players:
        player_names.append(p['name'])
        guardian_names += p['guardians']
        total_height += p['height']

    # format display strings
    header = f'Team: {team} Stats'
    stats_display = [
        f'Total players: {len(player_names)}\nPlayers:\n  {", ".join(player_names)}\n',
        f'Total guardians: {len(guardian_names)}\nGuardians:\n  {", ".join(guardian_names)}\n',
        f'Experienced players: {experienced}\nInexperienced players: {inexperienced}\n',
        f'Average team height: { round(total_height / len(players), 2)} inches'
    ]

    # display data
    print(header)
    print('-'*len(header))
    for s in stats_display: print(s)

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
        if main_choice == 3: 
            show_all_teams(teams)
            cont() 

        clear_screen()

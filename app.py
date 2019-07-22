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
        start = start+per_team
        stop = start+per_team

    return teams


if __name__ == '__main__':
    for dat in clean_data():
        team = dat['team']
        players = dat['players']

        print(f'Team: {team}')
        print('Players:')
        for player in players: print(player)
        print()



################################################################################
# Author: Jose Bucio
# Date: 04/04/2021
# Description: Programs to return the winner of the team from a specific year and
# return the number of wins from a specific team
################################################################################

def main():
    team_year = load_winners_data()
    #reconside to delete keys
    teams = team_year.keys()
    #teams.sort()
    team_wins = {}
    for team in teams:
        team_wins[team] = len(team_year[team])
    # start the count to wins
    #for team in team_year:
        #team_wins[team] = 0
    #for team in team_year:
        #team_wins[team] += 1

    year = int(input("Enter a year in the range 1903 -- 2020: "))
    if year < 1903 or year > 2020:
        print(f'Data for the year {year} is not included in this system.')
    elif year == 1904 or year == 1994:
        print(f'The World Series wasn\'t played in the year {year}.')
    else:
        #wins = {}
        #for current_wins in range(len(teams)):
            #wins[current_wins] += 1
            #team_year[year] = len(team_year[current_wins])
            #if team_year[team] = current_wins:
                #count += 1 team_year.get(year)
        print(f'The {team_year.get(year)} won the World Series in {year}.')
        print(f'They have won the World Series {team_wins[team]} times.')


def load_winners_data():
    with open('WorldSeriesWinners.txt', 'r') as foo:
        team_year = {}
        line = list(foo.readlines())
        #win_teams_list = []
        #start_year = 1903
        #win_team = list(foo.readline())
        #while(line):
        count = 0
        for index in range(len(line)):
            line[index] = line[index][:-1]
        #if line.strip() in team_year:
        #    team_year[line.strip()].append(start_year)
        #else:
        #    team_year[line.strip()] = [start_year]
        for start_year in range(1903, 2021):
            if start_year == 1994 or start_year == 1904:
                #start_year+=1
                continue
            team_year[start_year] = line[count]
            count +=1

    foo.close()
    return team_year

if __name__ == '__main__':
    main()

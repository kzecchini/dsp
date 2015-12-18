# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv


class Football(object):

    def __init__(self, file):
        self.file = file

    def read_data(self):
        f = open(self.file, 'rU')
        parsed_list = [row for row in csv.reader(f)]
        f.close()
        return parsed_list

    def get_min_score_difference(self, parsed_data):
        import math
        del parsed_data[0]
        score_diffs = [math.fabs(int(team_stats[5]) - int(team_stats[6])) for team_stats in parsed_data]
        return score_diffs.index(min(score_diffs))

    def get_team(self, index_value, parsed_data):
        return parsed_data[index_value][0]

# Testing output

test = Football('football.csv')
data = test.read_data()
minDiffIndex = test.get_min_score_difference(data)
team = test.get_team(minDiffIndex, data)

print team

# Output is Aston_Villa

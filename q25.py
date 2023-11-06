import pandas as pd

matches = pd.read_csv('matches.csv')
total_matches = matches['team1'].value_counts() + matches['team2'].value_counts()
wins = matches['winner'].value_counts()
win_ratio = wins / total_matches
print(win_ratio)
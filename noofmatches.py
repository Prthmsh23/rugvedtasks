import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')
total_matches = matches['team1'].value_counts() + matches['team2'].value_counts()
wins = matches['winner'].value_counts()
win_rate = (wins / total_matches) * 100

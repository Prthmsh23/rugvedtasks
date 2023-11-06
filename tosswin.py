import csv
import pandas as pd
df = pd.read_csv('matches.csv')
# Get the frequency of each team winning the toss
toss_winners = df['toss_winner'].value_counts()
# Find the team that won the most tosses
most_toss_wins = toss_winners.idxmax()

# Find the team that won the least tosses
least_toss_wins = toss_winners.idxmin()

print('Team that won the most tosses: ' ,most_toss_wins )
print('Team that won the least tosses: ',least_toss_wins)


toss_decisions = df.groupby(['toss_winner', 'toss_decision']).size()
print(toss_decisions)

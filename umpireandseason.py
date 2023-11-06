import pandas as pd
df = pd.read_csv('matches.csv')

umpires = pd.concat([df['umpire1'], df['umpire2'], df['umpire3']])
umpire_counts = umpires.value_counts()

umpire_max = umpire_counts.idxmax()

print('Umpire who did umpiring the maximum number of times:', umpire_max)

grouped = df.groupby('season')
matches_per_season = grouped['id'].count()
runs_per_season = grouped['win_by_runs'].sum()

print('Total number of matches in each season:\n', matches_per_season)
print('Total number of runs in each season:\n', runs_per_season)

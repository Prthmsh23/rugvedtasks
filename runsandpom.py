import pandas as pd
df = pd.read_csv('matches.csv')

idx_max = df['win_by_runs'].idxmax()
team_max = df.loc[idx_max, 'winner']

idx_min = df['win_by_runs'].idxmin()
team_min = df.loc[idx_min, 'winner']

venue_max = df.loc[idx_max, 'venue']
venue_min = df.loc[idx_min, 'venue']


print('Team that won with the highest number of runs:', team_max)
print('Venue where the team won with the highest number of runs:', venue_max)

print('Team that won with the lowest number of runs:', team_min)
print('Venue where the team won with the lowest number of runs:', venue_min)

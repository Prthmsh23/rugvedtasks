import pandas as pd
df = pd.read_csv('matches.csv')

match_counts = df['result'].value_counts()
print(match_counts)

tie_matches = df[df['result'] == 'tie'][["season",'team1', 'team2']]
print(tie_matches)

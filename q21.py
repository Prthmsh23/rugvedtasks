import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')

player_of_match = matches['player_of_match'].value_counts().head(10)
plt.figure(figsize=(12,6))
plt.bar(player_of_match.index, player_of_match.values, color ='blue')
plt.title('Top 10 Player of the Match Award Winners in IPL')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.xticks(rotation=60)
plt.show()

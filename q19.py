
import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')


dismissals = deliveries[deliveries['player_dismissed'].notna()]['dismissal_kind']


dismissals.value_counts().plot(kind='bar')
plt.title('Distribution of Dismissal Kinds')
plt.xlabel('Dismissal Kind')
plt.ylabel('Count')
plt.show()

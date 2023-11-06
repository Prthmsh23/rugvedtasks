import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

batsman_runs = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending = False).head(10)

plt.figure(figsize=(12,6))
plt.bar(batsman_runs.index, batsman_runs.values, color ='maroon')
plt.title('Top 10 run scorers in IPL')
plt.xlabel('Batsman')
plt.ylabel('Total Runs Scored')
plt.xticks(rotation=60)
plt.show()

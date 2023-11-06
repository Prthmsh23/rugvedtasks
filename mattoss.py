import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('matches.csv')
toss_decisions = df.groupby(['season', 'toss_decision']).size().unstack()
toss_decisions.plot(kind='bar', stacked=True)
plt.title('Toss decision across seasons')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

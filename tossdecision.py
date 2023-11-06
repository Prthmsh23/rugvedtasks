import pandas as pd
import numpy as np

matches = pd.read_csv('matches.csv')
toss_decisions = matches.groupby(['toss_winner', 'toss_decision']).size().reset_index(name='Count')
print(toss_decisions)
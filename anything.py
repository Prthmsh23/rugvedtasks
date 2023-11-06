import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('matches.csv')
df_2008 = df[df['season'] == 2008]
total_matches_2008 = df_2008.shape[0]
print("Total matches in 2008: ",str(total_matches_2008))
city_counts = df.groupby('city')['id'].count()
max_city = city_counts.idxmax()
min_city = city_counts.idxmin()

print("City with maximum matches: ",str(max_city))
print("City with minimum matches: ",str(min_city))

city_counts = df['city'].value_counts()
for city, count in city_counts.items():
   print('City: '+str(city)+', ' 'Matches: '+ str(count))


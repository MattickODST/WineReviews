# add your code here

import pandas as pd
print(pd.__version__)

data = pd.read_csv('c:/Users/The Madjutant/Desktop/CodeYou/Projects/wine-reviews-exercise-MattickODST/data/winemag-data-130k-v2.csv.zip')

#validate data
#print(data)

summary = data.groupby('country').agg(count=('country', 'size'),points=('points', 'mean'))

summary['points'] = summary['points'].round(1)

summary.to_csv("c:/Users/The Madjutant/Desktop/CodeYou/Projects/wine-reviews-exercise-MattickODST/data/reviews-per-country.csv")

#For testing purposes:
#print(summary)

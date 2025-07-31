import pandas as pd

data = pd.read_csv('population_data.csv')

# sort continent column
data.sort_values('Continent', inplace=True)

# creating multi-Index
data.set_index(['Continent', 'Country'], inplace=True)

print(data)
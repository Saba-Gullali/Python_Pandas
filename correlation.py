import pandas as pd
from scipy.stats import kendalltau


data = pd.read_csv('data.csv')
data = data.dropna(subset = ['Duration','Calories'])

Pearson_correlation = data['Duration'].corr(data['Calories'])
kendall_correlation = data['Duration'].corr(data['Calories'], method='kendall')
spearman_correlation = data['Duration'].corr(data['Calories'], method='spearman')
print(f"pearson correlation is : {Pearson_correlation}")
print(f"kendall correlation is : {kendall_correlation}")
print(f"spearman correlation is : {spearman_correlation}")






# string data
# converting data to dummy variable
# encoded_data = pd.get_dummies(data)

# finding correlation:
# correlation = encoded_data.corr()

# print(correlation)
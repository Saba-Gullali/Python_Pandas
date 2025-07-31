import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
# simple graph
# data.plot()

# scatter plot in which you need to identify x-axis and y-axis
data.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

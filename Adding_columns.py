#how to add columns in data Frame:
# adding ba single column ans calculated columns

import pandas as pd
data = pd.read_csv('string_data_only.csv')

hours_per_day = [1,2,3,4,5,6,7]
data['Hours/day'] = hours_per_day

pay_per_day = 1000
salary = data['Hours/day'] * pay_per_day
data['Salary'] = salary

data.to_csv('string_data_only.csv',index = False)


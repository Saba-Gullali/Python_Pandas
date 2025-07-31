import pandas as pd
data = pd.read_csv('string_data_only.csv')

# dropping row at index 1
drop_data = data.drop(index = 1)
to_file = drop_data.to_csv('string_data_only.csv', index=False)

# dropping column salary
drop_column = data.drop(columns = ['Salary'])

update_file = drop_column.to_csv('string_data_only.csv', index=False)
print(data.to_string())

# renaming row labels:
modified_row1 = data.rename(index={0:10})
print(modified_row1)

# for modifying the labels of multiple columns use mapper()
modified_row2_3 = data.rename(mapper={3:20,2:30})
print(modified_row2_3)
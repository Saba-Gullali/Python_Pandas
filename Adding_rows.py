# Data Manipulation
# How to add rows:
import pandas as pd
data = pd.read_csv('string_data_only.csv')

# adding a new row in the clean_data
# create a new single row:
new_row = pd.Series(data = ['justin bieber','new york','justinbie0@gmail.com',12345678789,'07-07-2025'],
                    index = ['Name','City','Email','Phone','Date'])

# converting series into data frame
new_data_frame = new_row.to_frame().T

# adding the row to the existing table
add_new_row = pd.concat([data,new_data_frame], ignore_index=True)

# adding new data frame to the file.
to_file = add_new_row.to_csv('clean_data.csv')

# adding multiple rows:
new_multiple_row = pd.DataFrame([{'Name':'justin bieber','City': 'new york','Email': 'justinbie0@gmail.com',
                         'Phone':12345678789,'Date': '07-07-2025'},
                        {'Name':'justin bieber2','City': 'new york2','Email': 'justinbie02@gmail.com',
                         'Phone':12345678789,'Date': '07-07-2025'}]
                       )

# adding to the file
add = pd.concat([data,new_multiple_row], ignore_index=True)
add_multiple_data = new_multiple_row.to_csv('string_data_only.csv')

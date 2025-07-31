# Basics of string data cleaning in python pandas:

import pandas as pd
data = pd.read_csv('string_data_only.csv')

# cleaning name column
data['Clean_name'] = data['Name'].str.strip().str.capitalize()

# cleaning city column
data['clean_city'] = data['City'].str.strip().str.capitalize()

# proper formatting of email column
# as username123@gmail.com or username123@domain.com

# email doen't contain any white spaces and must be in lower
data['Email'] = data['Email'].str.strip().str.lower()

# adding .com after @gmail and @domain
data['Email'] = data['Email'].str.replace(r'(?<=@gmail)$', '.com', regex = True)
data['Email'] = data['Email'].str.replace(r'(?<=@domain)$', '.com', regex = True)

# valid email values r'^[\w\.-]+@[\w\.-]+\.\w+$'
valid_email_values = r'^[\w\.-]+@[\w\.-]+\.\w+$'
valid_email = data['Email'].str.contains(valid_email_values,regex= True)


# validating phone
# replacing non digits
data['clean_Phone'] = data['Phone'].str.replace(r'\D', '', regex=True)

# standard format of xxx-xxx-xxxx
data['Standard_phone'] = data['clean_Phone'].apply(
    lambda x: f"{x[-10:-7]}-{x[-7:-4]}-{x[-4:]}"
    if len(x) >= 10 else x
)

# proper date
data['clean_Date'] = pd.to_datetime(data['Date'], format = 'mixed', dayfirst = True )

# creating a new dictionary of clean columns:
data_dict = {
    'Name': data['Clean_name'],
    'City': data['clean_city'],
    'Email': data['Email'],
    'Phone': data['Standard_phone'],
    'Date': data['clean_Date'],
    'hours\day': data['Hours/day'],
    'Salary' : data['Salary']

}

# new data frame of clean columns
new_df = pd.DataFrame(data_dict)
# new file of clean and proper format data:
new_file = new_df.to_csv('clean_data1.csv')

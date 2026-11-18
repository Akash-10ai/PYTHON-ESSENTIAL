import pandas as pd

x = {'Name': ['Rose', 'John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department':['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame

# access the value on the first row and first column
df.iloc[0, 0]

# access the value on the first row and third column
df.iloc[0, 2]

# access the column using the name
df.loc[0, 'Salary']


df2 = df
df2 = df2.set_index("Name")

# to display the first 5 rows of new dataframe
df2.head()

#  now, let us access the column using the name
df2.loc['Jane', 'Salary']

# SLICING IN PANDAS

# let us do the slicing using old dataframe df

df.iloc[0:2,0:3]

# lwt us do the slicing using the loc() function on old dataframe where index column labels as 0,1,2

df.loc[0:2, 'ID':'Department']


# let us do the slicing using loc() functions on new dataframe df2 where index column labels; Roe, John and jane

df2.loc['Rose': 'Jane', 'ID':'Department']


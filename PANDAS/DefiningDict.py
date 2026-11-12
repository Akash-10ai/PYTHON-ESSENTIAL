# first  import the pandas liabrary
import pandas as pd

# Define a dictionary 'x

x = {'Name': ['Rose', 'John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department':['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary':[100000, 80000, 50000, 60000]}

# casting the dictionary to a DataFrame
df = pd.DataFrame

# display the result df
df

# Retrieving the 'id' column ans assigning it to a variable x

x= df[['ID']]
x

# cheak type of x 
type(x)

# retrieving the Department, salary and id column and assigning it to a variable z

z = df[['Deppartment','Salary','ID']]
z
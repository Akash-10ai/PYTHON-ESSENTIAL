# Pandas program to rename column and row 

import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Rohan"],
    "City": ["Delhi", "Mumbai", "Pune"],
    "Marks": [85, 72, 90],
}
df = pd.DataFrame(data)
print("Original:")
print(df)

# Change one value (row 1, column Marks)
df.loc[1, "Marks"] = 80
print("\nAfter changing Diya's marks:")
print(df)

# Rename a column
df = df.rename(columns={"Name": "Student"})
print("\nAfter renaming Name to Student:")
print(df)

# Remove a column
df = df.drop(columns="City")
print("\nAfter dropping City:")
print(df)
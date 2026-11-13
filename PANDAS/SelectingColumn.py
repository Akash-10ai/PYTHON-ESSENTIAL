import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [20, 21, 19, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"],
})

print(df["Name"])              # one column
print(df[["Name", "City"]])    # multiple columns (note the double brackets)
print(df.loc[1])               # row with index label 1
print(df.loc[2, "City"])       # row 2, column "City"
print(df.iloc[0, 0])           # first row, first column (by position)
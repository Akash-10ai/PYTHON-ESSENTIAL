# pandas program to make a dataframe of student name, age and marks

import pandas as pd

# 1. Create a DataFrame
data = {
    "Name": ["Aarav", "Diya", "Rohan", "Sneha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 72, 90, 65],
}
df = pd.DataFrame(data)
print("Full table:")
print(df)

# 2. Select one column
print("\nOnly Name column:")
print(df["Name"])

# 3. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Fail"]
print("\nAfter adding Result column:")
print(df)

# 4. Filter rows
print("\nStudents with Marks above 70:")
print(df[df["Marks"] > 70])

# 5. Basic statistics
print("\nAverage marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
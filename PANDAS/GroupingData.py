<<<<<<< HEAD
# pandas program to group data

import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Rohan", "Sneha", "Karan", "Meera"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 72, 90, 65, 80, 78],
}
df = pd.DataFrame(data)

# Average marks of each department
print("Average marks per department:")
print(df.groupby("Department")["Marks"].mean())

# Highest marks in each department
print("\nHighest marks per department:")
=======
# pandas program to group data

import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Rohan", "Sneha", "Karan", "Meera"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 72, 90, 65, 80, 78],
}
df = pd.DataFrame(data)

# Average marks of each department
print("Average marks per department:")
print(df.groupby("Department")["Marks"].mean())

# Highest marks in each department
print("\nHighest marks per department:")
>>>>>>> e746f64fbecbe7aae80c695913befafb1744172c
print(df.groupby("Department")["Marks"].max())
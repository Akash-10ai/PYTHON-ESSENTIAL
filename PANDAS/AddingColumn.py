
#Python program to add two column of data set using panda
import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Maths": [85, 92, 45, 78],
    "Science": [78, 88, 52, 81],
})

df["Total"] = df["Maths"] + df["Science"]
print(df)

print("\nStudents with Total above 150:")
print(df[df["Total"] > 150])

print("\nSorted by Total (highest first):")
print(df.sort_values("Total", ascending=False))
import pandas as pd

df = pd.DataFrame({
    "Employee": ["Asha", "Ravi", "Meena", "Suresh", "Anil"],
    "Department": ["IT", "HR", None, "IT", "HR"],
    "Salary": [50000, None, 45000, 60000, None],
})

print("Missing values per column:")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(round(df["Salary"].mean(), 2))
df["Department"] = df["Department"].fillna("Unknown")

print("\nAfter cleaning:")
print(df)
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [20, 21, 19, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"],
}
df = pd.DataFrame(data)

print(df)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(2))


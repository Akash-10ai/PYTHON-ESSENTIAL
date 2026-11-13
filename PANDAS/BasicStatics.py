import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Maths": [85, 92, 45, 78],
    "Science": [78, 88, 52, 81],
})
df["Total"] = df["Maths"] + df["Science"]

print("Maths average:", df["Maths"].mean())
print("Maths highest:", df["Maths"].max())
print("Maths lowest: ", df["Maths"].min())
print("Maths sum:    ", df["Maths"].sum())

topper = df.loc[df["Total"].idxmax(), "Name"]
print("Topper:", topper)

print("\nAverage of each subject:")
print(df[["Maths", "Science"]].mean())
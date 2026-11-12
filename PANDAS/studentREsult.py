import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
    "Maths": [85, 92, 45, 78, 60],
    "Physics": [78, 88, 52, 81, 55],
    "Chemistry": [90, 95, 35, 70, 65],
}
df = pd.DataFrame(data)

subjects = ["Maths", "Physics", "Chemistry"]
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = (df["Total"] / 300 * 100).round(2)
df["Result"] = df[subjects].min(axis=1).apply(lambda m: "Pass" if m >= 40 else "Fail")

print(df)
print("\nTopper:", df.loc[df["Percentage"].idxmax(), "Name"])
print("Students passed:", (df["Result"] == "Pass").sum())
print("\nSubject averages:")
print(df[subjects].mean())
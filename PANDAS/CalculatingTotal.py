<<<<<<< HEAD
# pandas liabray to calculate total of product

import pandas as pd

data = {
    "Product": ["Pen", "Notebook", "Bag", "Pencil"],
    "Price": [10, 50, 500, 5],
    "Quantity": [5, 3, 1, 10],
}
df = pd.DataFrame(data)

# Multiply two columns to make a new one
df["Total"] = df["Price"] * df["Quantity"]
print(df)

=======
# pandas liabray to calculate total of product

import pandas as pd

data = {
    "Product": ["Pen", "Notebook", "Bag", "Pencil"],
    "Price": [10, 50, 500, 5],
    "Quantity": [5, 3, 1, 10],
}
df = pd.DataFrame(data)

# Multiply two columns to make a new one
df["Total"] = df["Price"] * df["Quantity"]
print(df)

>>>>>>> e746f64fbecbe7aae80c695913befafb1744172c
print("\nGrand total:", df["Total"].sum())
import pandas as pd

# Table 1: student details
students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aarav", "Diya", "Rohan", "Sneha"],
})

# Table 2: marks of the students
marks = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [85, 72, 90, 65],
})

print("Students table:")
print(students)

print("\nMarks table:")
print(marks)

# Combine both tables using the common column "ID"
combined = pd.merge(students, marks, on="ID")
print("\nCombined table:")
print(combined)

# Now we can use the combined table as usual
print("\nStudents with Marks above 70:")
print(combined[combined["Marks"] > 70])
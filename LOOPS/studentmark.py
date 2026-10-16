students = ["Aman", "Rahul", "Priya", "Rohit", "Neha"]
marks = [75, 82, 90, 65, 88]

search_name = input("Enter student name: ")

for i in range(len(students)):
    print("Checking:", students[i])

    if students[i].lower() == search_name.lower():
        print("Student found!")
        print("Name:", students[i])
        print("Marks:", marks[i])
        break

else:
    print("Student not found!")

print("Program ended.")
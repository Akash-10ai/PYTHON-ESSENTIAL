class Student:
    # Class attribute: shared by ALL objects of this class
    college = "ABC Institute of Technology"

    # Constructor: runs automatically when an object is created
    def __init__(self, name, roll_no, marks):
        # Instance attributes: unique to each object
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Instance method: behavior of the object
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40


# Creating objects (instantiation)
s1 = Student("Aman", 101, 78)
s2 = Student("Riya", 102, 35)

# Accessing attributes and calling methods
s1.display()               # Name: Aman, Roll No: 101, Marks: 78
s2.display()               # Name: Riya, Roll No: 102, Marks: 35

print(s1.is_pass())        # True
print(s2.is_pass())        # False

print(s1.college)          # ABC Institute of Technology
print(s2.college)          # ABC Institute of Technology
class EMployee:
    count = 0

def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    EMployee.count += 1

def give_raise(self, percent):
    self.salary += self.salary * percent / 100


e1 = EMployee("Aman", 50000)
e2 = EMployee("Riya", 60000)
e3 = EMployee("karan", 55000)

print(EMployee.count)  # Output: 3

e1.give_raise(10)
print(e1.salary)
print(e2.salary)

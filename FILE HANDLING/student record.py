# pyhon program for student record manager 

FILE = "students.txt"

def add_student(name, marks):
    with open(FILE, "a") as f:
        f.write(f"{name},{marks}\n")

def show_students():
    try:
        with open(FILE) as f:
            print(f"{'Name':<15}{'Marks':>5}")
            print("-" * 20)
            for line in f:
                name, marks = line.strip().split(",")
                print(f"{name:<15}{marks:>5}")
    except FileNotFoundError:
        print("No records yet.")

def topper():
    best_name, best_marks = None, -1
    with open(FILE) as f:
        for line in f:
            name, marks = line.strip().split(",")
            if int(marks) > best_marks:
                best_name, best_marks = name, int(marks)
    print(f"Topper: {best_name} ({best_marks})")

add_student("Asha", 91)
add_student("Ravi", 78)
add_student("Meera", 95)
show_students()
topper()
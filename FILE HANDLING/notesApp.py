FILE = "notes.txt"

def add_note():
    note = input("Enter note: ")
    with open(FILE, "a") as f:        # append so old notes are kept
        f.write(note + "\n")
    print("Note saved.")

def view_notes():
    try:
        with open(FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No notes yet.")
        return

    if not lines:
        print("No notes yet.")
        return

    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

def delete_note():
    try:
        with open(FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No notes to delete.")
        return

    view_notes()
    try:
        num = int(input("Note number to delete: "))
    except ValueError:
        print("Please enter a number.")
        return

    if 1 <= num <= len(lines):
        lines.pop(num - 1)             # remove from the list
        with open(FILE, "w") as f:     # rewrite the whole file
            f.writelines(lines)
        print("Note deleted.")
    else:
        print("Invalid number.")

def count_notes():
    try:
        with open(FILE, "r") as f:
            print("Total notes:", len(f.readlines()))
    except FileNotFoundError:
        print("Total notes: 0")

while True:
    print("\n1. Add  2. View  3. Delete  4. Count  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        count_notes()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
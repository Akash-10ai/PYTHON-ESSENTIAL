users = {"admin": "pass123", "student": "cse2026"}

def login():
    attempts = 3
    while attempts > 0:
        try:
            username = input("Username: ")
            password = input("Password: ")

            if users[username] != password:
                raise PermissionError("Wrong password")

            print(f"Welcome, {username}!")
            return True

        except KeyError:
            print("User does not exist.")
        except PermissionError as e:
            print(f"Login failed: {e}")

        attempts -= 1
        print(f"Attempts left: {attempts}\n")

    print("Account locked. Too many failed attempts.")
    return False

login()
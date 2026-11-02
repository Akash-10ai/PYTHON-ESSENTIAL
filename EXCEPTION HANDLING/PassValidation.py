class WeakPassworsError(Exception):
    pass

try:
    password = input("Enter a password")

    if len(password) < 8:
        raise WeakPasswordError("password must be contain at least 8 characters")

    print("Password Accepted")

except WeakPasswordError as e:
    print("Password Error:", e)

finally:
       print("Password validation completed")

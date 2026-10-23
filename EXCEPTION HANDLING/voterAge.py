def valid_voterAge(age):
    """VAlidate if the provided age meets the requirement for voting .
    Raises ValueError for invalid age values.
    """
    if age <= 0:
        raise("valid voter: age cannot be negative")
    elif age >= 18:
        print("valid voter: you are eligible to vote")
    else:
        print("Invalid voter: you age is less than 18")

def main():
    try:

        user_input = input("please enter your age:")
        age = int(user_input)

        valid_voterAge(age)

    except ValueError as e:

        if "Invalid literal" in str(e):
            print("Error: please a valid numerical number for age")
        else:
            print("f Error: {e}")


if __name__ == "__main__":
    main()
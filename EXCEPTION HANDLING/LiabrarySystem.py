class LibraryError(Exception):
    """Base class for all library-related errors."""

class BookNotFoundError(LibraryError):
    pass

class BookAlreadyIssuedError(LibraryError):
    pass

library = {"Python Basics": True, "Data Structures": False, "Operating Systems": True}
# True = available, False = already issued

def issue_book(title):
    if title not in library:
        raise BookNotFoundError(f"'{title}' is not in the library")
    if not library[title]:
        raise BookAlreadyIssuedError(f"'{title}' is already issued")
    library[title] = False
    print(f"'{title}' issued successfully")

for title in ["Python Basics", "Data Structures", "Machine Learning", "Python Basics"]:
    try:
        issue_book(title)
    except BookNotFoundError as e:
        print("Not found:", e)
    except LibraryError as e:
        print("Library problem:", e)
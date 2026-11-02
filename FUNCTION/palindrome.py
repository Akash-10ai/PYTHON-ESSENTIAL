def is_palindrome(text):

    cleaned_text = ''.join(text.split()).lower()

    return cleaned_text == cleaned_text[::-1]


user_input = input("enter a word , number or phrse")

if is_palindrome(user_input):
    print(f" yes, '{user_input}' is a palindrome")
    
else:
    print(f"no, '{user_input}' is not a palindrome")      
          
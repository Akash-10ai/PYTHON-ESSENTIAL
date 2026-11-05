def char_types(filename):
    vowels = consonants = digits = 0
    with open(filename) as f:
        for ch in f.read().lower():
            if ch in "aeiou":
                vowels += 1
            elif ch.isalpha():
                consonants += 1
            elif ch.isdigit():
                digits += 1
    print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}")

char_types("sample.txt")
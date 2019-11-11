# Task1
# Write a function is_palindrome which takes a string and returns boolean
# whether the string is a palindrome or not


def is_palindrome(word: str) -> bool:
    if len(word) > 1:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
    else:
        return True


print(is_palindrome("thagjjgaht"))
print(is_palindrome("fgyugj"))
print(is_palindrome("pap"))


# Task 2
# Write a function copy_string which takes a string and recursively, character
# by character creates a copy of it.


def copy_string(string: str) -> str:
    if len(string) > 1:
        return string[0] + copy_string(string[1:])
    else:
        return string[0]


print(copy_string("bla bla bla!"))


# Task 3
# Write a function first_letter which takes a string and returns first
# uppercase letter in it


def first_letter(string: str) -> str:
    if string[0].isupper():
        return string[0]
    else:
        return first_letter(string[1:])


print(first_letter("hello my name is Dasha А"))

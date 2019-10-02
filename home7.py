# Write a function using list comprehensions that takes a list of strings
# and removes those that contain 4 characters or less


def remove_shorts(strings):

    return [x for x in strings if len(x) > 4]



assert remove_shorts(['telegram', 'sport', 'call', 'football', 'jet']) \
       == ['telegram', 'sport', 'football']
assert remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope']) \
       == ['zombie', 'vision', 'telescope']

Write a function using list comprehensions that takes a string and changes
letter's case from upper to lower and vice versa


def change_case(string):

    return "".join([x.upper() if x.islower() else x.lower() for x in string])


assert change_case("HELLO") == "hello"
assert change_case("Hi! I'm Jim :)") == "hI! i'M jIM :)"
assert change_case("welcome y'all") == "WELCOME Y'ALL"


# Write a function using dict comprehensions that takes a list of strings
# and outputs a dictionary where keys are strings and values are booleans
# that say whether the word is a palindrome or not


def detect_palindromes(strings: list) -> dict:
    return {x: x == x[::-1] for x in strings}

assert detect_palindromes(['madam', 'joy', 'fish']) == {
    'madam': True,
    'joy': False,
    'fish': False
}

assert detect_palindromes(['print', 'mom', 'dad']) == {
    'print': False,
    'mom': True,
    'dad': True
}

# Write a function that takes 2 dictionaries where keys are cars and values
# are their prices. The function checks whether the sum of prices in 1
# dictionary is equal to the sum in the 2nd


def compare_prices(cars1: dict, cars2: dict) -> bool:

    return sum(cars1.values()) == sum(cars2.values())


assert compare_prices({'BMW': 20000, 'Nissan': 15000},
                      {'Mustang': 30000, 'Renault': 5000}) is True
assert compare_prices({'Volvo': 13000, 'Infinity': 80000},
                      {'Ford GT': 100000, 'Lada': 3000}) is False



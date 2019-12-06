import re


# 4. Write a Python program that matches a string that has
# an a followed by zero or one 'b'.


def find_match1(string):
    return len(re.findall(r'a[0b]', string)) > 0


print(find_match1("abbab"))
print(find_match1("ab"))
print(find_match1("a0"))
print(find_match1("a"))


# 10. Write a Python program that matches a word at the beginning of a string


def find_first_word(string):
    return re.findall(r"^\w+", string)


print(find_first_word("Hello my name is Peter"))
print(find_first_word("Hello! my name is Peter"))
print(find_first_word("Hello, my name is Peter"))


# 11. Write a Python program that matches a word at end of string,
# with optional punctuation.


def find_last_word(string):
    return re.findall(r"\w+\S*$", string)


print(find_last_word("Hello, my name is Peter"))
print(find_last_word("Hello, my name is Peter!!!"))
print(find_last_word("Hello, my name is Peter."))
print(find_last_word("Hello, my name is Peter "))


# 16. Write a Python program to remove leading zeros from an IP address.


def remove_zeros(string):
    string = re.sub(r"\.[0]*", ".", string)
    return string


print(remove_zeros("234.004.045"))
print(remove_zeros("134.004.345"))
print(remove_zeros("234.104.045"))


# 42. Write a Python program to find urls in a string.

def get_url(string):
    return re.findall("https?://\S*", string)


print(get_url("These are my urls:"
              " https://docs.python.org https://www.w3resource.com sure"))


# 50. Write a Python program to remove the parenthesis area in a string.
# Go to the editor Sample data : ["example (.com)", "w3resource",
# "github (.com)", "stackoverflow (.com)"]
# Expected Output:
# example
# w3resource
# github
# stackoverflow


def remove_parenthesis(listy):
    return [re.sub(r" ?(\(\.?\w+\))", "", item) for item in listy]


print(remove_parenthesis(["github (.com)", "stackoverflow (.com)"]))

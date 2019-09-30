# task 1


def insert_whitespace(sentence):
    new_sentence = ""

    for letter in sentence:
        if letter.isupper() and sentence.index(letter) != 0:
            letter = " " + letter
        new_sentence += letter
    return new_sentence


print(insert_whitespace("SheWalksToTheBeach"))


# task 2

def calculate(num1, num2, option):
    calc_dict = {
        "sum": num1 + num2,
        "div": num1 / num2,
        "substract": num1 - num2,
        "multiply": num1 * num2
    }

    return calc_dict[option]


print(calculate(15, 15, 'sum'))


# task 3


def wraps(string, width):
    new_line = ""
    len_line = len(string) // width
    i = 0

    for k in range(0, len_line + 1):
        new_line = f'{new_line} {string[i:i + width]} \n'
        i += width

    return new_line


print(wraps("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))


# task *


def custom_split(string, delimiter):
    new = string.find(delimiter, 0)
    new_list = []
    del_len = len(delimiter)
    i = 0

    if new == 0:
        string = string[new + del_len::]
        new = string.find(delimiter, i)
    while new != -1:
        new_list.append(string[0:new])
        string = string[new + del_len::]
        new = string.find(delimiter, i)
        i += 1
    if len(string) > del_len:
        new_list.append(string)
    return new_list


print(custom_split(" my name is Dasha ", " "))

# task 1


def del_str(string, key):
    return string.replace(key,"")
print(del_str("Hey! I'm glad y'all came today!", "a"))


# task 2


names = ["John",  "Kate",  "Dave",  "Den", "Adele"]
user = input("Enter your name: ")

if user not in names:
    print("Not Found")
elif user in names and names.index(user) % 2 == 0:
    print("It's all good")
else:
    names.remove(user)
    print(names)

# task 3


start_list = [75, 81, 96, 213, 94, 15, 38, 11]

while sum(start_list) >= 200:
    start_list.pop(len(start_list) - 1)
print(start_list)

# task 4

num = int(input("Number: "))

while True:
    print(int(num))
    if num == 1:
        break
    elif num % 2 == 0:
        num = num / 2
    else:
        num = num * 3 + 1
# task 1.1 no replace
def fin_list(line, number):
    word_list = ", ".join(x for x in line.split(", ") if int(x[:1:-4]) != number)
    return word_list

print(fin_list("test1, test2, test3, test4, test5", int(input("Your number: "))))

# task 1.2 with replace
def fin_list2(line, number):
    if number == "1":
        repl_line = "test" + number + ", "
    elif number == line[len(line)-1]:
        repl_line = ", " + "test" + number
    else:
        repl_line = "test" + number
    return line.replace(repl_line, "").replace(", ,",",")
print(fin_list2("test1, test2, test3, test4, test5", input("Your number: ")))
# task 2

def domain(url):
    http_stat = url.find("//") + 2
    clean_http = url[http_stat::]
    work_list = clean_http.split("/")

    return work_list[0].replace("www.", "")

print(domain("https://realpython.com/courses/python-thonny/"))

# task 3
import random

rand_line = random.randint(0, 10)
user_input = input("Please enter your number from 0 to 10: ")
print(rand_line == user_input)




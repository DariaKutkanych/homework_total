from random import randint

# Extend the existing @logger decorator which writes logs to a file
# called log.txt instead of console

with open("files/log.txt", "w") as f:
    pass


def logger(func):
    def wrapper(*args):
        with open("files/log.txt", "a") as f1:
            f1.write(f"{func(*args)} \n")

    return wrapper


@logger
def writer(string):
    return string


writer("print")
writer("print")

# Write a function called new_lines that takes a file path, opens the file
# and adds a newline character (\n) once in 20 symbols


def new_lines(path: str):
    new_text = ""
    with open(path, "r") as f2:
        size = f2.read(20)
        while len(size) > 0:
            new_text += f'{size}\n'
            size = f2.read(20)
        with open(path, "w") as fnew:
            fnew.write(new_text)


new_lines("files/new_text.txt")


# Add a new method to our Worker-Boss program to the Boss class.
# This method is called (dump_workers). It must take all workers from
# workers list and output them into a .csv file (just the way we did it)
#
# Extra point for doing it using built-in csv library
# Extra point for doing it using 3rd party library pandas

with open("files/workers.csv", "w") as f:
    f.write("id,Name,company")


class Boss:
    def __init__(self, name: str, company: str):
        self.id = randint(1000, 9999)
        self.name = name
        self.company = company
        self.workers = []

    def dump_workers(self):
        for worker in self.workers:
            with open("files/workers.csv", "a") as f3:
                f3.write(f'\n{worker.id},{worker.name},{worker.company}')


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id = randint(1000, 9999)
        self.name = name
        self.company = boss.company
        self._boss = boss
        self._boss.workers.append(self)

    def __repr__(self):
        return f"'\n'{self.name} {self.id} {self.company}"

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self._boss.workers.remove(self)
            self._boss = value
            self.company = value.company
            self.boss.workers.append(self)


bos1 = Boss("John", "Apple")
bos2 = Boss("Peter", "Google")
work1 = Worker("Peter", bos1)
work2 = Worker("Mark", bos1)

bos1.dump_workers()

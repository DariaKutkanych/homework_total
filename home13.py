# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):
# methods:
#   - to_int
#   - to_str
#   - to_bool
#   - to_float
#
# Don't forget to use @wraps


from functools import wraps


from random import randint


class TypeDecorators:
    @staticmethod
    def to_int(function):
        @wraps(function)
        def wrapper(*args):
            return int(function(*args))
        return wrapper

    @staticmethod
    def to_bool(function):
        @wraps(function)
        def wrapper(*args):
            return bool(function(*args))
        return wrapper

    @staticmethod
    def to_str(function):
        @wraps(function)
        def wrapper(*args):
            return str(function(*args))
        return wrapper

    @staticmethod
    def to_float(function):
        @wraps(function)
        def wrapper(*args):
            return float(function(*args))
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True


# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
# id_ - is just a random unique integer


class Boss:
    def __init__(self, name: str, company: str):
        self.id = randint(1000, 9999)
        self.name = name
        self.company = company
        self.workers = []


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id = randint(1000, 9999)
        self.name = name
        self.company = boss.company
        self._boss = boss
        self._boss.workers.append(self)

    def __repr__(self):
        return f"{self.name} {self.id} {self.company}"

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
work2 = Worker("Mark", bos2)

work1.boss = bos2

print(work1.company)
print(work1.boss.company)
print(bos2.workers, "Bos2")
print(bos1.workers, "Bos1")

work1.boss = bos1

print(bos2.workers, "Bos2")
print(bos1.workers, "Bos1")

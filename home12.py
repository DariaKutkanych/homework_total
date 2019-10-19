# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"

from functools import wraps


def logger(f):
    @wraps(f)
    def wrapper(*args):
        return f'{f.__name__} called with {", ".join(str(ag) for ag in args)}'
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))
print(square_all(3, 4, 6, 7))

# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_func = func(*args, **kwargs)
            for word in words:
                if word in new_func:
                    new_func = new_func.replace(word, "*")
            return new_func
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type_ != type(result):
                print("Type does not match")
                return False
            elif max_length < len(args[0]):
                print("The text is too long")
                return False
            elif len([x for x in contains if x in result]) < 0:
                print("The text does not contain all the info")
                return False
            else:
                return result
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

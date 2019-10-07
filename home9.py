# Implement a class Mathematician which is a helper class for doing math
# operations on lists
# The class doesn't take any attributes and only has methods:
#   - square_nums (takes a list of integers and returns the list of squares)
#   - remove_positives (takes a list of integers and returns it without
# positive numbers
#   - filter_leaps (takes a list of dates (integers) and removes those that
# are not 'leap years'


class Mathematician:

    def __init__(self):
        pass

    def square_nums(self, numbers):
        return [number**2 for number in numbers]

    def remove_positives(self, positives):
        return [num for num in positives if num < 0]

    def filter_leaps(self, years):
        return [x for x in years if x % 4 == 0]


m = Mathematician()


assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


# Write a class Product that has 4 attributes:
#   - type
#   - name
#   - price
#   - quantity

# and the following methods:
#   - add(amount) - adds a specified quantity of a single product
#   - set_discount(percent) - adds a discount for current product.
# discount must be specified in percentage


class Product:
    def __init__(self, type1, name, price, quantity):
        self.type1 = type1
        self.name = name
        self.price = price
        self.quantity = quantity

    def add(self, amount):
        self.quantity += amount

    def set_discount(self, percent):
        self.price = self.price*((100 - percent)/100)


p = Product('Sport', 'Football T-Shirt', 100, 30)


assert p.quantity == 30
p.add(90)
assert p.quantity == 120

assert p.price == 100
p.set_discount(25)
assert p.price == 75

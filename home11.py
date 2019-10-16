# Implement a simple composition of 4 classes: ATM, Client, Card, Bank
#
# Bank(name) + accounts = [] - list of all accounts opened in the current bank
# methods:
#   open_account(client: Client) - takes an instance of Client class as an
# argument and creates a new instance of Card bound to this client (and returns
# it). ! A client can only open one account per bank !
#   close_account(card: Card) - removes specified instance of Card
#
# ATM(bank: Bank, amount: float) - takes an instance of Bank class as an
# argument (the bank this card is bound to) and the amount of money in
# the current ATM.
# methods:
#   withdraw(card: Card, sum: float) - takes two arguments: an instance of
# Card and sum which is needed to be withdrawn. You should consider 2 cases:
#       1) when the amount of money in the bank is less than the sum
#       2) when the ATM and Card are bound to different banks (it shouldn't
# let you withdraw)
#   add(card: Card, sum: float) - add the specified amount of money to the card
#   change_pin(card: Card, old_pin: int, new_pin: int) - change card's pin
#
# Card(account: int, balance: float, pin: int, owner: Client, bank: Bank) -
# account is just a random 5-digit number. Pin is 0000 by default
# methods:
#   transfer_money(card, amount) - transfers the money from the current card to
# the specified one
#
# Client(name: str) + cards = [] - list of cards bound to the client
# methods:
#   show_total_balance - returns the sum of money from all cards owned by the
# client


class ATM:
    def __init__(self, bank, amount):
        self.amount = amount
        self.bank = bank

    def withdraw(self, card, sum):
        if sum < card.balance:
            if self.bank == card.bank:
                card.balance -= sum

    def add(self, card, sum):
        card.balance += sum

    def change_pin(self, card, old_pin, new_pin):
        if card.pin == old_pin:
            card.pin = new_pin


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, client, account, pin, balance = 0):
        card = Card(account, balance, pin, client, self)
        self.accounts.append(card)
        client.cards.append(card)
        return card

    def close_account(self, card):
        self.accounts.remove(card)


class Client:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def show_total_balance(self):
        return sum([x.balance for x in self.cards])


class Card:
    def __init__(self, account, balance, pin, owner, bank):
        self.account = account
        self.balance = balance
        self.pin = pin
        self.owner = owner
        self.bank = bank

    def transfer_money(self, card, amount):
        self.balance -= amount
        card.balance +- amount


client = Client("John")
bank = Bank("PrivatBank")
atm = ATM(bank, 10000)

card = bank.open_account(client, "First acct", 12345)
assert card.balance == 0.0

atm.add(card, 500)
assert card.balance == 500.0
print(card.balance)


atm.withdraw(card, 100)
print(card.balance)
atm.change_pin(card, 12345, 54321)
print(card.pin)
print(bank.accounts[0].account)
# bank.close_account(card)
# print(bank.accounts)
print(client.show_total_balance())




# Write a function called choose_func which takes a list of nums and 2
# callback functions. If all nums inside the list are positive, execute the
# first function on that list and return the result of it. Otherwise return the
# result of the second one


def choose_func(nums, func1, func2):
    f = func1
    for num in nums:
        if num < 0:
            f = func2
            break
    return f(nums)


# Assertions


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


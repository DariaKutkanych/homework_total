# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
# Book class and adds the book to books list for current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
# the specified author
# - group_by_year(year: int) - returns a list of all books grouped by the
# specified year

# All 3 classes must have a readable __repr__ method!

# Also, book class should have a class variable which holds the amount of
# all existing books

# Task 2 extends the first one. Now you should add 2-3 types of books (for
# example, Schoolbook, Magazine etc)

# Library class should still have only one list for all books in contains
# but different methods for grouping by types. For example:
#   - fetch_schoolbooks
#   - fetch_magazines


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f'Library: {self.name}. Books: {[x.name for x in self.books]}.'\
               f' Authors: {[x.name for x in self.authors]}'

    def new_book(self, name, year, author, btype):
        book = Book(name, year, author, btype)
        self.books.append(book)
        Book.total_count += 1
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [x for x in self.books if x.author == author]

    def group_by_year(self, year):
        return [x for x in self.books if x.year == year]

    def fetch_schoolbooks(self):
        return [x for x in self.books if x.type == "Schoolbook"]

    def fetch_magazines(self):
        return [x for x in self.books if x.type == "Magazine"]


class Book:

    total_count = 0

    def __init__(self, name, year, author, btype):
        self.name = name
        self.year = year
        self.author = author
        self.btype = btype

    def __repr__(self):
        return f'{self.name} {self.year} {self.author} {self.btype}'


class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f'{self.name} {self.country} {self.birthday}'


auth1 = Author("Peter Bolt", "Italy", "23.12.1900")
auth2 = Author("John Frank", "Spain", "12.01.1700")
libr1 = Library("Best one")
bk1 = Book("Name", 200, auth2, "Magazine")


libr1.new_book("Long stories", 1923, auth1, "Schoolbook")
libr1.new_book("Short stories", 1960, auth1, "Schoolbook")
libr1.new_book("Fairy tales", 1740, auth2, "Magazine")
libr1.new_book("Novels", 1960, auth2, "Magazine")


print(libr1)
print(auth1)
print(libr1.group_by_year(1960))
print(libr1.group_by_author(auth2))
print(libr1.fetch_magazines())
print(libr1.fetch_schoolbooks())
print("Total amount of books: ", Book.total_count)

from abc import ABC


class AbstractDataStructure(ABC):
    def __init__(self, maxsize):
        self.a__items = {}
        self.maxsize = maxsize

    def sorted_dict(self):
        return sorted(self.a__items.items())

    def reverse_sorted_dict(self):
        items_copy = self.sorted_dict().copy()
        new_list = []
        while items_copy:
            new_list.append(items_copy.pop())
        return new_list

    def join(self, joiner):
        k = ""
        for key, value in self.a__items.items():
            k += f"({key},{value}){joiner}"
        return k[:-len(joiner)]

    def index(self, key):
        for b, a in enumerate(self.sorted_dict()):
            if a[0] == key:
                return b

    def last_index(self, key):
        index = len(self.sorted_dict()) - 1
        while index > 0:
            if key == self.sorted_dict()[index]:
                return index

    def sum(self):
        k = 0
        for key in self.a__items.keys():
            k += int(key)
        return k

    def is_empty(self):
        return not bool(len(self.a__items))

    def is_full(self):
        return len(self.a__items) == self.maxsize


class Queue(AbstractDataStructure):

    def enqueue(self, value):
        try:
            s = int(max(self.a__items.keys())) + 1
            for i in range(len(self.a__items)):
                self.a__items[str(s)] = self.a__items[str(s-1)]
                s -= 1
        except ValueError:
            pass
        self.a__items["0"] = value
        if self.is_full():
            self.dequeue()

    def dequeue(self):
        s = self.sorted_dict()[-1][0]
        self.a__items.pop(s)


class Stack(AbstractDataStructure):

    def push(self, value):
        if self.is_full():
            s = int(max(self.a__items.keys()))
            key = str(s)
            self.a__items[key] = value
        else:
            if len(self.a__items) > 0:
                s = int(max(self.a__items.keys())) + 1
                key = str(s)
                self.a__items[key] = value
            else:
                self.a__items["0"] = value

    def pop(self):
        s = self.sorted_dict()[-1][0]
        self.a__items.pop(s)

# b = Stack(5)

# b.push("hey")
# b.push("ho")
# b.push("ha")
# b.push("hi")
# b.push("hr")
# b.push("hf")
# b.push("hd")


# print(b.a__items)
# print(len(b.a__items))
# print(b.is_full())
# b.pop()
# print(b.a__items)
# print(b.sum())
# print(b.join(" "))
# print(b.sorted_dict())
# print(b.reverse_sorted_dict())
# print(b.reverse_sorted_dict())

# q = Queue(5)
# print(q.a__items)
# q.enqueue("3")
# q.enqueue("4")
# q.enqueue("5")
# q.enqueue("8")
# q.enqueue("9")
# print(q.a__items)

class PriorityQueue:
    def __init__(self):
        self.priority = []

    def insert(self, priority, word):
        self.priority.append((priority, word))

    def get_highest_priority(self):
        return sorted(self.priority)[0]

    def delete_highest_priority(self):
        return self.priority.pop(self.priority.index(self.get_highest_priority()))


k = PriorityQueue()
k.insert(3, "Mike")
k.insert(2, "Peter")
k.insert(1, "Ralf")
k.insert(5, "Steve")
print(k.get_highest_priority())
print(k.delete_highest_priority())
print(k.priority)
k.insert(1, "Steve")
print(k.priority)

from abc import ABC


class Person(ABC):
    def __init__(self, id, name, company):
        self.id = id
        self.name = name
        self.company = company


class Boss(Person):
    def __init__(self, id, name: str, company: str):
        super().__init__(id,name,company)
        self.workers = []

    def __repr__(self):
        return f"{self.name} {self.id} {self.company}"


class Worker(Person):
    def __init__(self, id, name: str, company: str, boss):
        super().__init__(id, name, company)
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

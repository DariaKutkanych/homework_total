from abc import ABC


class Warrior(ABC):
    def __init__(self, name, health, army):
        self.name = name
        self._health = health
        self._is_alive = True
        self.army = army
        self.damage = 0

    def __repr__(self):
        return f'{self.name} | {self.health}|{self.army}|alive {self.is_alive}'

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value
        if not self._is_alive:
            self.army.warriors.remove(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self.is_alive = False
            print(f'{self.name} is dead')

    @staticmethod
    def hit(warrior):
        if warrior.is_alive:
            if isinstance(warrior, Archer):
                warrior.health -= warrior.damage*1.5
            else:
                warrior.health -= warrior.damage


class Swordsman(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 25


class Archer(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 10


class Army(ABC):
    def __init__(self):
        self.warriors = []

    def train_swordsman(self, name, health) -> Swordsman:
        soldier = Swordsman(name, health, self)
        self.warriors.append(soldier)
        return soldier

    def train_archer(self, name, health) -> Archer:
        soldier = Archer(name, health, self)
        self.warriors.append(soldier)
        return soldier


class DarkArmy(Army):
    def __repr__(self):
        return f'dark army'


class LightArmy(Army):
    def __repr__(self):
        return f'light army'

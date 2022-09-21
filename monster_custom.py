from monster import Monster

class Magician(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.health = 20
        self.power = 0

class Wolf(Monster):
    pass

class Giant(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.power = self.power * 2
        self.health = self.health / 2

class CerberusHead(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.power = self.power * 1.5
        self.health = self.health * 1.5

class Hades(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.power = self.power * 3
        self.health = self.health * 3
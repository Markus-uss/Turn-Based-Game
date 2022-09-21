from abc import ABC, abstractmethod, abstractproperty

class ShopItem(ABC):
    @abstractproperty
    def price(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def change(self, hero):
        pass

    def __str__(self):
        return f"{self.name} ({self.price} gold)"

class BigHealingPotion(ShopItem):
    name = "big healing potion"
    price = 3
    def change(self, hero):
        hero.health = hero.health + 50
    
class SmallHealingPotion(ShopItem):
    name = "small healing potion"
    price = 1
    def change(self, hero):
        hero.health = hero.health + 10

class WeaponUpgrade(ShopItem):
    name = "weapon upgrade"
    price = 1
    def change(self, hero):
        hero.power = round(hero.power * 1.05, 2)

class OminousToken(ShopItem):
    name = "ominous token"
    price = 5
    def change(self, hero):
        hero.obtained_token = True

class BoltOfZeus(ShopItem):
    name = "bolt of zeus"
    price = 10
    def change(self, hero):
        hero.power = round((hero.power*2),2)

class ShieldOfAegis(ShopItem):
    name = "shield of aegis"
    price = 12
    def change(self, hero):
        hero.health = (hero.health + 25)*2

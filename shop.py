#Author: Markus Lu A01224733

from hero import Hero
from shop_item import BigHealingPotion, SmallHealingPotion, WeaponUpgrade, OminousToken, BoltOfZeus, ShieldOfAegis

class Shop():
    #Generates limited items for the store from a txt file.
    def __init__(self, textfile: str = 'shop.txt'):
        with open(textfile,'r') as data:
            items = data.read()
            items = items.split('\n')
            self.items = []
            for item in items:
                if item == 'big healing potion':
                    self.items.append(BigHealingPotion())
                elif item == 'small healing potion':
                    self.items.append(SmallHealingPotion())
                elif item == 'weapon upgrade':
                    self.items.append(WeaponUpgrade())
                elif item == 'ominous token':
                    self.items.append(OminousToken())
                elif item == 'bolt of zeus':
                    self.items.append(BoltOfZeus())
                elif item == 'shield of aegis':
                    self.items.append(ShieldOfAegis())
                else:
                    pass

    #Return all the available items in the store in a presentable format.
    def __str__(self):
        message = 'Welcome to the shop. The following items are available:'
        item_display = []
        items = enumerate(self.items,1)
        for count,item in items:
            item_display.append(f'{count} - {item.name} ({item.price} gold)')

        message = message + '\n' + '\n'.join(item_display)
        return message

    #Return the number of items in the store.
    def __len__(self):
        return len(self.items)

    #Returns all the available items within the store.
    @property
    def available_items(self):
        shop_list = []
        index = -1
        for item in self.items:
            index += 1
            shop_list.append(f'[{index}] ' + type(item).__name__)
        return shop_list

    #If the item is in the store, return item.
    def buy(self, shopitem):
        shopitem = int(shopitem)
        if shopitem < len(self.items) and shopitem >= 0:
            return self.items.pop(shopitem)
        else:
            raise IndexError("Number must be between 0 and {len(self.items)}")

if __name__=="__main__":
    pass
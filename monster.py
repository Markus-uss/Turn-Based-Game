#Author: Markus Lu A01224733
import random

class Monster():
    #Sets up basic attributes for monster.
    def __init__(self, level):
        if type(level) != int:
            raise AttributeError("Level needs to be an integer.")
        self.health = 10 + level * 10
        self.power = level * 5
    
    #Checks if the monster health point is above 0
    @property
    def is_alive(self):
        return self.health > 0

    #Returns information on the monster's status and current stats.
    def __str__(self):
        if self.is_alive:
            return f'{type(self).__name__} ({self.health:.2f} health, {self.power:.2f} power)'
        else:
            return f'{type(self).__name__} (DEAD)'

    #Compares the abilities of a monster with another.
    def __lt__(self, other):
        if isinstance(other, Monster):
            return (self.health, self.power) < (other.health, other.power)
        else:
            raise TypeError('The compared entity must be from monster class.')

if __name__=="__main__":
    pass
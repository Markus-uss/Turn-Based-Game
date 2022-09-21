#Author: Markus Lu A01224733

import random
from monster import Monster
from monster_team import MonsterTeam

class Hero():
    #Sets up the basic attributes to the hero class.
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.power = 50
        self.gold = 0
        self.dodge_stack = 1

        #Story Related
        self.obtained_token = False

    #Checks if the hero's health point is above 0.
    @property
    def is_alive(self):
        return (self.health>0)

    #Decrease dodge stack by 1 if it is greater than 1.
    @property
    def update_dodge_stack(self):
        if self.dodge_stack > 1:
            self.dodge_stack -= 1
        return self.dodge_stack
    
    #Return hero statistical information.
    def get_description(self):
        return (f'{self.name} ({int(self.health)}HP, {self.power}AP)')

    #Reduce hero and monsters health points. Both sides attack each other.
    #Reduce dodge stacks by 1.
    def attack(self, team):
        if isinstance(team, MonsterTeam) == False:
            raise TypeError("Enemy needs to be from the monster team.")
        for enemy in team._monsters:
            if enemy.is_alive:
                enemy.health = round((enemy.health - (self.power)),1)
                self.health -= enemy.power
        self.dodge_stack = self.update_dodge_stack

    #Reduce hero and monsters health points. Monsters attack power is reduced.
    #Reduce dodge stacks by 1.
    def block(self, team):
        if isinstance(team, MonsterTeam) == False:
            raise TypeError("Enemy needs to be from the monster team.")
        for enemy in team._monsters:
            if enemy.is_alive:
                self.health -= (enemy.power * 0.3)
                enemy.health = round((enemy.health - (self.power * 0.5)),1)
        self.dodge_stack = self.update_dodge_stack

    #90% chance to dodge individual enemy attacks, decrease chance by 10% per turn use.
    def dodge(self, team):
        if isinstance(team, MonsterTeam) == False:
            raise TypeError("Enemy needs to be from the monster team.")
        damage_taken = False
        self.dodge_stack += 1
        for enemy in team._monsters:
            if enemy.is_alive:
                hit_chance = random.randint(1,10)
                if hit_chance <= 1*self.dodge_stack:
                    self.health -= enemy.power
                    damage_taken = True
        
        #If 0 damage is taken that turn, deal double your power as damage to all enemies.
        if damage_taken == False:
            print('\nYou have successfully dodged, and attacked the monsters.')
            for enemy in team._monsters:
                if enemy.is_alive:
                    enemy.health = round((enemy.health - (self.power * 2)),1)
        if damage_taken == True:
            print('\nYou stubbed your toe and the monsters ganged up on you.')


if __name__=="__main__":
    pass
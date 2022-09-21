from monster_custom import Wolf,Magician,Giant,CerberusHead,Hades
from monster import Monster
import operator

class MonsterTeam():
    #Generates a monsters based on the given levels.
    def __init__(self, level: int):
        self._monsters = list()
        filename = r'levels\level_' + str(level) +'.txt'
        with open(filename,'r') as data:
            monsters = data.read()
            monsters_list = monsters.split('\n')
        for monster in monsters_list:
            monster_info = monster.split(':')
            if monster_info[1].isdigit:
                if monster_info[0] == 'wolf':
                    self._monsters.append(Wolf(int(monster_info[1])))
                elif monster_info[0] == 'giant':
                    self._monsters.append(Giant(int(monster_info[1])))
                elif monster_info[0] == 'magician':
                    self._monsters.append(Magician(int(monster_info[1])))
                elif monster_info[0] == 'cerberushead':
                    self._monsters.append(CerberusHead(int(monster_info[1])))
                elif monster_info[0] == 'hades':
                    self._monsters.append(Hades(int(monster_info[1])))
            else:
                raise TypeError('Monster level must be a number.')


    #Checks if any monsters are alive.
    @property
    def is_alive(self):
        for monster in self._monsters:
            if monster.is_alive == True:
                return True
        return False

    #Returns all alive monsters sorted from highest health to lowest.
    @property
    def alive_monsters(self):
        monster_alive = list()
        for monster in self._monsters:
            if monster.is_alive:
                monster_alive.append(monster)
        return sorted(monster_alive,key=operator.attrgetter('health'),reverse=True)

    #Returns the monster with the most health points.
    @property
    def healthiest_monster(self):
        healthiest_monster = 'pending'
        for monster in self._monsters:
            if healthiest_monster == 'pending':
                healthiest_monster = monster
            elif monster.health > healthiest_monster.health:
                healthiest_monster = monster
        return healthiest_monster

    #Returns the monster with the lowest attack power.
    @property
    def weakest_monster(self):
        weakest_monster = 'pending'
        for monster in self._monsters:
            if weakest_monster == 'pending':
                weakest_monster = monster
            elif monster.power < weakest_monster.power:
                weakest_monster = monster
        return weakest_monster
    
    #Returns the total health of the monster team.
    @property
    def health(self):
        total_health = 0
        for monster in self._monsters:
            total_health += monster.health
        return total_health

    #Returns the total power of the monster team.
    @property
    def power(self):
        total_power = 0
        for monster in self._monsters:
            if monster.health > 0:
                total_power += monster.power
        return total_power

    #Returns information on monster team.
    def __str__(self):
        message = f'{len(self.alive_monsters)}/{len(self._monsters)} monsters:'
        monsters = sorted(self._monsters,key=operator.attrgetter('health'), reverse=True)
        for monster in monsters:
            message = message + '\n' + str(monster)
        return message

    #Returns a single monster that is alive.
    def get_alive_monster(self):
        for monster in self._monsters:
            if monster.is_alive == True:
                return monster
    
    #Enemies apply passive effects, wolves increase other wolves attack by 1, 
    #magicians heals the team by 10% excluding magicians
    def next_turn(self):
        wolf_count = 0
        magician_count = 0
        for monster in self._monsters:
            if monster.is_alive == True:
                if (type(monster).__name__)[:4].lower() == 'wolf':
                    wolf_count += 1
                elif (type(monster).__name__)[:8].lower() == 'magician':
                    magician_count += 1
        
        for monster in self._monsters:
            if monster.is_alive:
                if (type(monster).__name__)[:8].lower() != 'magician' and magician_count > 0:
                    monster.health = round((monster.health * 1.1),1)
                if (type(monster).__name__)[:4].lower() == 'wolf' and wolf_count > 1:
                    monster.power += (1 * wolf_count)

import random

import game_data
from ASCII_RPG.weapon import Weapon, claws, jaws, short_bow, orc_blade, scythe, silver_bow, iron_sword, sharp_claws, mythril_bow, dragon_claws, xcal


bosses = []
enemies = []
minions = []
elites = []


class Enemy:
    def __init__(self, name: str, health: int, exp: int, weapon: Weapon, gold: int):
        assert isinstance(weapon, Weapon), f"weapon is not a Weapon instance: {weapon}"
        self.name = name
        self.health = health
        self.exp = exp
        self.weapon = weapon
        self.gold = gold

    def attack(self, hero):
        if random.randint(0, 100) <= game_data.Luck_Chance:
            print("You dodged the enemies attack!")
        else:
          damage = self.weapon.damage
          hero.health -= damage
          print(f"{self.name} dealt {damage} damage to {hero.name}.")
          if hero.health > 0:
            print(f"{hero.name} has {hero.health} health remaining.")
          else:
            print(f"{hero.name} has been defeated!")
            exit()#fix this


class Minion(Enemy):
    def __init__(self, name, health, exp, weapon, gold):
        super().__init__(name, health, exp, weapon, gold)
        self.max_health = health

        minions.append(self)

class Elites(Enemy):
    def __init__(self, name, health, exp, weapon, gold):
        super().__init__(name, health, exp, weapon, gold)
        self.max_health = health
        
        elites.append(self)
        
class Boss(Enemy):
    def __init__(self, name, health, exp, weapon, gold):
        super().__init__(name, health, exp, weapon, gold)
        self.max_health = health
        bosses.append(self)

rat = Minion("Rat", 3, 5, claws, 2)
slime = Minion("slime", 6, 5,  jaws, 3)
wolf = Minion("wolf", 10, 6, claws, 5)
goblin = Minion("goblin", 15, 10,  short_bow, 5)
troll = Minion("troll", 14, 7, short_bow, 6)
rage_elf = Minion("Rage Elf", 15, 8, silver_bow, 10)
zombie = Minion("zombie", 12, 7, iron_sword, 8)

ogre = Elites("ogre", 35, 15, orc_blade, 25)
reaper = Elites("reaper", 45, 22, scythe, 25)
wyvern = Elites("wyvern", 40, 18, scythe, 22)
demon = Elites("demon", 50, 35, scythe, 45)
imp = Elites("imp", 30, 17, orc_blade, 20)
dire_wolf = Elites("dire wolf", 27, 14, sharp_claws, 15)

dragon = Boss("Dragon Boss", 150, 200, dragon_claws, 200)


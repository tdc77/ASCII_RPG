from weapon import *
import random
import game_data


class Hero:
    def __init__(self, name: str, health: int, total_exp: int, level: int, gold: int, weapon: Weapon):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.total_exp = total_exp
        self.level = level
        self.gold = gold
        

    def attack(self, enemy):
        damage = self.weapon.damage 
        enemy.health -= damage
        print(f"{self.name} dealt {damage} damage to {enemy.name}.")
        if enemy.health > 0:
            print(f"{enemy.name} has {enemy.health} health remaining.")
        else:
            print(f"{enemy.name} has been defeated!")
            print(f"You got {enemy.exp} experience and {enemy.gold} gold!")
            if random.randint(0, 100) < 20 and self.level <= 5:
                game_data.pot += 1
                print("You've found a potion!")
            if random.randint(0, 100) < 20 and self.level > 5:    
                 game_data.megapotion += 1
                 print("You found a megapotion!")


         





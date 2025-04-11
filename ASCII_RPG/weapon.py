from random import randint
import game_data

class Weapon:
    def __init__(self, name: str, type: str, damage: int, value: int = 0):
        self.name = name
        self.type = type
        self.value = value
        self.damage_min = max(damage - 2, 1)
        self.damage_max = damage + 2

    @property
    def damage(self) -> int:
        return randint(self.damage_min, self.damage_max) + game_data.ATK
iron_sword = Weapon("Iron_sword", "Sword",  4,  8)
short_bow = Weapon("s_bow", "bow", 4,  3)
silver_sword = Weapon("silver_sword", "sword0", 7, 10)
silver_bow = Weapon("silver bow", "bow", 6, 10)
mythril_sword = Weapon("Mythril_Sword", "sword", 11, 25)
mythril_bow = Weapon("Mythril Bow", "bow", 10, 25)
xcal = Weapon("Xcal", "sword", 20, 150)
# Enemy weps ________________________________________________________#
orc_blade = Weapon("orc blade", "sword", 10, 0)
scythe = Weapon("scythe", "reaper", 16, 0)
fist = Weapon("fists", "hand",  2, 0)
claws = Weapon("claws", "claws", 3, 0)
sharp_claws = Weapon("sharp claws", "claws", 12, 0)
jaws = Weapon("jaws","sharp", 3, 0)
dragon_claws = Weapon("dragon claws", "claws", 27, 0)
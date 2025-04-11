import os, random
from enemy import minions, elites, bosses
from character import Hero
from ASCII_RPG.weapon import iron_sword, silver_sword, mythril_sword, short_bow, silver_bow, orc_blade, scythe
import game_data
from PIL import Image

hero = Hero("Warrior", 40, 0, 1, 0, iron_sword)



run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

gold = 0
x = 0
y = 0



        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],   # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],   # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],   # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],   # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"],   # y = 4
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],   # y = 5
       ["forest",   "fields",   "plains",   "forest",   "forest",    "hills",   "mountain"]]   # y = 6



y_len = len(map)-1
x_len = len(map[0])-1


biom = {
    "plains": {
        "t": "PLAINS",
        "e": True,
        "c": False},
    "forest": {
        "t": "WOODS",
        "e": True,
        "c": True},
    "fields": {
        "t": "FIELDS",
        "e": False,
        "c": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True,
        "c": False},
    "town": {
        "t": "TOWN CENTRE",
        "e": False,
        "c": False},
    "shop": {
        "t": "SHOP",
        "e": False,
        "c": False},
    "mayor": {
        "t": "MAYOR",
        "e": False,
        "c": False},
    "cave": {
        "t": "CAVE",
        "e": False,
        "c": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True,
        "c": True},
    "hills": {
        "t": "HILLS",
        "e": True,
        "c": False,
    }
}



def clear():
    os.system("cls")


def draw():
    print("xX--------------------xX")


def save():
    list = [
        hero.name,
        str(hero.health),
        str(game_data.ATK),
        str(game_data.pot),
        str(hero.total_exp),
        str(hero.gold),
        str(x),
        str(y),
        str(key),
        str(hero.level),
        str(game_data.megapotion)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if hero.health + amount < hero.health_max:
        hero.health += amount
    else:
        hero.health = hero.health_max
    print(hero.name + "'s HP refilled to " + str(hero.health) + "!")

def weaponshop():
    while True:
        print("Welcome to the weapon shop!")
        print("Xx--------------------------------xX")
        print("1. Buy Weapon")
        print("2. Upgrade Weapon (+1ATK) 160 Gold")
        print("3. Leave")
        wep_choice = input("> ")

        if wep_choice == "1":
            if hero.level < 6:
                print("1. Buy silver sword - 50 Gold")
                print("2. Buy Short Bow - 40 Gold")
                print("3. Leave")
            else:
                print("4. Buy Mythril Sword - 145 Gold")
                print("5. Buy Silver Bow - 100 Gold")
                print("6. Leave")
            buy_op = input("> ")

            if buy_op == "1":
                if hero.gold >= 50:
                    hero.weapon = silver_sword
                    hero.gold -= 50
                else:
                    print("You don't have enough gold")
                    input("> ")
            elif buy_op == "2":
                if hero.gold >= 40:
                    hero.weapon = short_bow
                    hero.gold -= 40
                else:
                    print("You don't have enough gold!")
                    input("> ")
            elif buy_op == "3" or buy_op == "6":
                break
            elif buy_op == "4":
                if hero.gold >= 145:
                    hero.weapon = mythril_sword
                    hero.gold -= 145
                else:
                    print("You don't have enough gold!")
                    input("> ")
            elif buy_op == "5":
                if hero.gold >= 100:
                    hero.weapon = silver_bow
                    hero.gold -= 100
                else:
                    print("You don't have enough gold!")

        elif wep_choice == "2":
            if hero.gold >= 160:
                game_data.ATK += 1
                hero.gold -= 160
            else:
                print("You don't have enough gold!")
                input("> ")

        elif wep_choice == "3":
            break

    shop()


def battle():
    global fight, boss
    # Select enemy based on hero level
    
    if hero.level < 6:
        enemy = random.choice(minions)  # Only minions for heroes below level 6
    else:
        enemy2 = minions.extend(elites) # all enemies are in play now!
        enemy = random.choice(enemy2)  # Elites for level 6 and above

    enemy.health_max = enemy.health

    if boss:
        enemy = bosses

    while fight:
        clear()
        draw()
        print(f"Defeat the {enemy.name}!")
        draw()
        print(f"{enemy.name}'s HP: {enemy.health}/{enemy.health_max}")
        print(f"Level: {hero.level}")
        print(f"{hero.name}'s HP: {hero.health}/{hero.health_max}")
        print(f"Potions: {game_data.pot}")
        print(f"TotalXP: {hero.total_exp}")
        print(f"Level: {hero.level}")
        draw()
        print("1 - ATTACK")

        if game_data.pot > 0:
            print("2 - USE POTION (30HP)")

        draw()

        choice = input("# ")

        if choice == "1":
            hero.attack(enemy)
            if enemy.health > 0:
                enemy.attack(hero)

        elif choice == "2" and game_data.pot > 0:
            game_data.pot -= 1
            heal(30)
            print(f"{hero.name} heals for 30 HP!")
            enemy.attack(hero)

        elif choice == "2":
            print("No potions!")

        else:
            print("Invalid choice!")

        input("> ")  # This ensures player action before proceeding

        # Check defeat conditions
        if hero.health <= 0:
            print(f"{enemy.name} defeated {hero.name}...")
            print("GAME OVER")
            fight = False

        elif enemy.health <= 0:
            hero.gold += enemy.gold
            hero.total_exp += enemy.exp
            fight = False
            check_level_up()
            enemy.health = enemy.max_health  # Reset enemy health

def check_level_up():
    level_amount = hero.level * 100
    if hero.total_exp >= level_amount:
        print("You have leveled up!!")
        input('> ')
        print('Max Health + 10')
        hero.health_max += 10
        hero.health = hero.health_max # fill health at level up
        input('> ')
        if game_data.Luck_Chance < 51:
          print('Dodge Chance + 1')
          game_data.Luck_Chance += 1
        else:
            print("Dodge chance is maxed out!!")  # 50 is max
        input('>')
        if game_data.ATK < 51:
          print('ATK + 1')
          game_data.ATK += 1
        else:
            print(" Your ATK is maxed out!!")  # 50 is max
        input('> ')
        if hero.level < 21:
           hero.level += 1
           hero.total_exp = 0 #reset hero xp to start next level xp
        else:
            print(" You are at max level!")
            hero.total_exp = 0 #reset hero xp to start next level xp 

def shop():
    global buy, gold

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("GOLD: " + str(hero.gold))
        print("POTIONS: " + str(game_data.pot))
        print("ATK: " + str(game_data.ATK))
        draw()
        print("1 - BUY POTION (30HP) - 20 GOLD")
        print("2 - LUCK CHANCE(Dodge) + 1 - 65 GOLD")
        if hero.level > 6:
          print("3 - BUY MEGA POTION(70HP) - 75 Gold")
        print("4 - WEAPON SHOP")
        print("5 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if hero.gold >= 20:
                game_data.pot += 1
                hero.gold -= 20
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if hero.gold >= 65:
                game_data.Luck_Chance += 1
                hero.gold -= 65
                print("You've upgraded dodge chance")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if hero.gold >= 70:
                game_data.megapotion += 1
                hero.gold -= 70
                print("You've upgraded dodge chance")
            else:
                print("Not enough gold!")
            input("> ")
                
        elif choice == "4":
            weaponshop()
        elif choice == "5":
            buy = False


def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if game_data.ATK < 12:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False

def show_map_image():
    """Opens the saved map image."""
    map_image = Image.open("newmap.png")  # Ensure the filename matches your screenshot
    resized_image = map_image.resize((800, 400))
    resized_image.show()
def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False



while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("I'm the creator of this game and these are the rules. There is a dragon in a cave, you must defeat it!" )
            print(" However the Mayor of the town will only give you the key if he thinks you are strong enough!!")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What's your name, hero? ")
            hero.name = name
            print(f"Hello {hero.name} you find yourself in a strange land, you notice a iron sword nearby and you equip it, you can hear what sounds like a town far away.")
            input()
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 10:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    game_data.ATK = int(load_list[2][:-1])
                    game_data.pot = int(load_list[3][:-1])
                    hero.total_exp = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    level = int(load_list[9][:-1])
                    megapotion = int(load_list[10][:-1])
                    clear()
                    print("Welcome back, " + hero.name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()


        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + hero.name)
            print("HP: " + str(hero.health) + "/" + str(hero.health_max))
            print("Level: "+ str(hero.level))
            print("ATK: " + str(game_data.ATK))
            print("POTIONS: " + str(game_data.pot))
            print("GOLD: " + str(hero.gold))
            print("TotalXP: " + str(hero.total_exp))
            print("COORD:", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if game_data.pot > 0:
                print("5 - USE POTION (30HP)")
            if y > 0 or x > 0:
                print("6 - Map")    
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if game_data.pot > 0:
                    game_data.pot -= 1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                show_map_image()
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()

            else:
                standing = True




    
             

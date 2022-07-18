from items import *
import random

class Character:
    def __init__(self, health, power, gold, xp, armor):
        self.armor = armor
        self.xp = xp
        self.health = health
        self.power = power
        self.gold = gold

    def attack(self, enemy):
        enemy.get_hit_by(self)
        if enemy.alive() == False:
            print(f"The {type(enemy).__name__} is dead.")

    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f"The {type(self).__name__} has {self.health} health and {self.power} power.")
    
    def get_hit_by(self, enemy):
        if self.armor > 0:
            if enemy.power - self.armor < 0:
                print("Your armor prevents damage being done")
            else:
                print(f"The {type(enemy).__name__} does {enemy.power} damage to the {type(self).__name__}, you block {self.armor} damage.")
                self.health -= enemy.power - self.armor
        else:
            print(f"The {type(enemy).__name__} does {enemy.power - self.armor} damage to the {type(self).__name__}.")
            self.health -= enemy.power

class Hero(Character):
    next_level = 20
    max_health = 10
    def __init__(self, health = max_health, power = 2, level = 1, gold = 200, xp = 0, armor = 0):
        super(Hero, self).__init__(health, power, gold, xp, armor) 
        self.level = level
        self.gold = gold
        self.inv = [Weapon('Rusty sword', 2, 2, 1), SuperTonic(10, 1), Evade(15, 1)]
        self.curr_weapon = self.inv[0]
        self.power = self.curr_weapon.power

    def inventory(self):
        self.print_inventory()
        while True:
            picker = int(input("""
                Inventory
            ======================
            What do you want to do?
            1. List Inventory
            2. Equip weapon
            3. Use a potion
            9. Exit backpack\n> """)
            )
            if picker == 1:
                self.print_inventory()
            elif picker == 2:
                self.equip_item()
            elif picker == 3:
                self.potions_menu()
            elif picker == 4:
                self.print_inventory()
            elif picker == 9:
                print("Closing backpack!")
                break
            else:
                print("That's not a valid option")

    def print_inventory(self):
        print(f"You have {self.gold} coins")
        if self.inv != []:
            print("\tInside your backpack you have:")
            for item in self.inv:
                print(f"\t\t{str(item)}")
        else:
            print("Your backpack is empty.")
        print(f"You have your {self.curr_weapon.name} equipped")

    def print_stats(self):
        print(f"""
                You are a level {self.level} {type(self).__name__} with {self.gold} gold coins
                You have {self.health}/{self.max_health} health
                You do {self.power} damage with the {self.curr_weapon.name} and have {self.armor} armor
                You have {self.xp} xp, {self.next_level - self.xp} more xp until level {self.level + 1}""")
        
    def equip(self, item):
        self.inv.remove(item)
        self.inv.insert(0, item)
        self.curr_weapon = self.inv[0]
        self.power = self.curr_weapon.power
        print(f"{item.name} has now been equipped")

    def equip_item(self):
        desired_item = input("What item would you like to equip?\n> ")
        for item in self.inv:
            if item.equippable and (item.name.lower() == desired_item.lower()):
                self.equip(item)
                break
        else:
            print("Sorry, you don't have a weapon with that name. Make sure you entered the item name correctly")

    def potions_menu(self):
        equippable_inv = [item for item in self.inv if not item.equippable]
        inv_str = '\n'.join([str(item) for item in equippable_inv])
        print(f"Usable Items:\n{inv_str}")

        desired_item = input("What potion would you like to use?\n> ")
        for item in self.inv:
            if (not item.equippable) and (str(item).lower() == desired_item.lower()):
                item.use(self)
                break
        else:
            print("Sorry, you don't have a potion with that name. Make sure you entered the item name correctly")
    
    def level_up(self):
        if self.xp >= self.next_level:
            self.max_health += 5
            self.power += 5
            self.level += 1
            self.next_level += 20
            print(f"""
                  You have leveled up! You are now level {self.level}
                  Your max health increses 5 points to {self.max_health}
                  Your power increases 5 points to {self.power}
                  You need {self.next_level} xp for level {self.level + 1}""")
            self.xp = 0

    def fight(self):
        enemylist = [Goblin(), Zombie(), Bear(), Rat(), Giant()]
        enemy = random.choice(enemylist)
        
        if self.health <= 0:
            print("You can't fight right now, go to the bar and heal up before trying again")
        else:
            print(f"A wild {type(enemy).__name__} has appeared!\n")
        
        while enemy.alive() and self.alive():
            print()
            self.print_status()
            enemy.print_status()
            picker = input(f"""
            What do you want to do?
            1. Fight {type(enemy).__name__}
            2. Open backpack
            3. Do nothing
            9. flee\n>""")
            if picker == "1":
                self.attack(enemy)
                if enemy.alive():
                    enemy.attack(self)
                else:
                    print(f"The {type(enemy).__name__} dropped {enemy.gold} gold and {enemy.xp} xp")
                    self.gold += enemy.gold
                    self.xp += enemy.xp
                    self.level_up()
            elif picker == '2':
                self.print_inventory()
                res = input(f"""Do you want to:
                1. Use a potion
                2. Swap weapon
                3. Return to the fight
                """)
            elif picker == '1':
                self.potions_menu()
            elif picker == "3":
                pass
            elif picker == "9":
                print("You got away.")
                break
            else:
                print("That's not a valid option")


class Enemy(Character):
    def __init__(self, health = 10, power = 2, gold = 2, reward = 2, xp = 5, armor = 0):
        super(Enemy, self).__init__(health, power, gold, xp, armor) 
        self.reward = reward


class Berzerker(Hero):
    def attack(self, enemy):
        super().attack(enemy)
        prob = random.randint(1,10)
        if prob <= 2:
            print("The hero hit a critical strike!")
            return super().attack(enemy)

class Shadow(Hero):
    def get_hit_by(self, enemy):
        prob = random.randint(1,10)
        if prob <= 2:
            print("You dodged the attack!")
        else:
            return super().get_hit_by(enemy)

class Medic(Hero):
    def attack(self, enemy):
        super().attack(enemy)
        prob = random.randint(1,10)
        if prob <= 2:
            self.health = self.health + 2
            print("The medic healed himself")

class Wizard(Hero):
    pass


class Goblin(Enemy):
    pass

class Giant(Enemy):
    def __init__(self, health = 50, power = 20, gold = 20, reward = 10, xp = 40, armor = 0):
        super(Giant, self).__init__(health, power, gold, reward, xp, armor)

class Bear(Enemy):
    def __init__(self, health = 20, power = 6, gold = 20, reward = 2, xp = 20, armor = 0):
        super(Bear, self).__init__(health, power, gold, reward, xp, armor) 

class Zombie(Enemy):
    def get_hit_by(self, enemy):
            print("This enemy is undead...")
            return super().get_hit_by(enemy)
    
    def alive(self):
        return True

class Rat(Enemy):
    def __init__(self, health = 1, power = 1, gold = 20, reward = 2, xp = 10, armor = 0):
        super(Rat, self).__init__(health, power, gold, reward, xp, armor) 

    def get_hit_by(self, enemy):
        prob = random.randint(1,10)
        if prob <= 9:
            print("The rat is too small and too fast to hit! You missed it! :)")
        else:
            return super().get_hit_by(enemy)

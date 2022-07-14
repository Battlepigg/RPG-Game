# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        # self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {type(self).__name__} does {self.power} damage to the {type(enemy).__name__}.")
        if enemy.health <= 0:
            print(f"The {type(enemy).__name__} is dead.")

    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f"The {type(self).__name__} has {self.health} health and {self.power} power.")

class Hero(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    pass

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    zombie = Zombie(100, 1)
    # hero.health = 10
    # hero.power = 5
    # goblin.health = 6
    # goblin.power = 2

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        # print(f"You have {hero.health} health and {hero.power} power.")
        # print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            # Hero attacks goblin
            # Goblin.health -= Hero.power
            # print("You do {} damage to the goblin.".format(Hero.power))
            # if Goblin.health <= 0:
            #     print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            # hero.health -= goblin.power
            # print("The goblin does {} damage to you.".format(goblin.power))
            # if hero.health <= 0:
            #     print("You are dead.")

main()


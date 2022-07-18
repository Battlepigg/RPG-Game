'''
TODO
    add evade variable
    add stuff to the store
    balance health, power of all characters
    
    OPTIONAL
    add sell functionality
    make swap potion
    make enemies drop items as well as gold

'''
import os
from characters import *
from items import *

def bar(_hero):
    while True:
        picker = int(input("""
            Welcome to the Bar!
            ======================
            What do you want to do?
            1. Get a drink (heal)
            2. Talk to the locals
            9. Exit bar\n> """)
        )
        if picker == 1:
            _hero.health = _hero.max_health
            print(f"Your health has been healed to {_hero.health}")

        elif picker == 2:
            locals = ["Be careful around town, the bears have made their way to the valley!",
                      "These pesky rats are really annoying, I wish someone would do something about them...",
                      "I've heard rumors of giants, hopefully I never see one face to face"]
            print(random.choice(locals))

        elif picker == 9:
            print("Thanks for visiting!")
            break
        else:
            print("That's not a valid option")

def main():
    '''Main execution'''
    char_list = [['Medic', '20% chance to heal Yourself.', Medic()],
                ['Shadow', '10% chance not to get hit.', Shadow()],
                ['Berzerker', '20% chance to deal double damage.', Berzerker()]]
    #os.system('clear')
    while True:
        idx = 1
        print("\t\tChoose your character")
        for char in char_list:
            print(f"\t{idx}. {char[0]} : {char[1]}")
            idx += 1
        res = input('\n>')
        if (int(res) > 0) and (int(res) < len(char_list) + 1):
            _hero = char_list[int(res)-1][2]
            print(f"You are a level 1 {type(_hero).__name__}")
            break
        else:
            print("That is not a valid option")

    store = Store(_hero)

    print("It is pitch black. You are likely to be eaten by a grue.")

    while True:

        picker = input("""
                Town Square
            ======================
            What do you want to do?
            1. Explore
            2. Visit the store
            3. Visit the bar
            4. Manage inventory
            5. View stats
            9. Exit game\n> """)
        if picker == '1':
            _hero.fight()
        elif picker == '2':
            store.go_shopping(_hero)
        elif picker == '3':
            bar(_hero)
        elif picker == '4':
            _hero.inventory()
        elif picker == '5':
            _hero.print_stats()
        elif picker == '9':
            print("Thanks for playing!")
            quit()
        else:
            print("That's not a valid option!")

if __name__ == "__main__":
    main()
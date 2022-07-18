'''
TODO
    add armor to store
    add evade variable
    make swap potion
    add stuff to the store
    balance health, power of all characters
    make the fucking thing not run twice
    
    OPTIONAL
    add sell functionality
    make swap potion
    make enemies drop items as well as gold



'''

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
            5. Exit bar\n> """)
        )
        if picker == 1:
            _hero.health = _hero.max_health
            print(f"Your health has been healed to {_hero.health}")

        elif picker == 2:
            pass

        elif picker == 5:
            print("Thanks for visiting!")
            break

def main():
    '''Main execution'''

    ########### DOGSHIT
    char_list = [['Medic', 'Chance to heal Yourself.', Medic()],
                ['Shadow', '10 chance not to get hit.', Shadow()],
                ['Berzerker', '20 chance to deal double damage.', Berzerker()]]

    idx = 1
    print("Who would you like to play as?")
    for char in char_list:
        print(f"\t{idx}. {char[0]} : {char[1]}")
        idx += 1
    print(end='\n>')
    res = int(input())
    _hero = char_list[res-1][2]
    print(f"You are a level 1 {type(_hero).__name__}")

    store = Store(_hero)
    ########### DOGSHIT

    print("It is pitch black. You are likely to be eaten by a grue.")

    while True:

        picker = int(input("""
            What do you want to do?
            1. Explore
            2. Visit the store
            3. Visit the bar
            4. Manage inventory
            5. Exit game\n> """))
        if picker == 1:
            _hero.fight()
        elif picker == 2:
            store.go_shopping(_hero)
        elif picker == 3:
            bar(_hero)
        elif picker == 4:
            _hero.inventory()
        elif picker == 5:
            print("Thanks for playing!")
            quit()

if __name__ == "__main__":
    main()
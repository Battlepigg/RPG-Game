class Item():
    pass

class Weapon(Item):
    def __init__(self, name, price, power, level):
        self.name = name
        self.price = int(price)
        self.power = power
        self.level = level
        self.equippable = True

    def __str__(self):
        return self.name

class Potion(Item):
    def __init__(self, price, level):
        self.price = int(price)
        self.level = level
        self.equippable = False
    
    def use(self):
        pass

class SuperTonic(Potion):
    def __init__(self, price, level):
        super(SuperTonic, self).__init__(price, level)

    def use(self, hero):
            hero.health = hero.max_health
            print(f"Your health has been restored to {hero.max_health}.")
    
    def __str__(self):
        return "Super tonic"


class Evade(Potion):
    def __init__(self, price, level):
        super(Evade, self).__init__(price, level)

    # add 2 onto the hero's evade
    def __str__(self):
        return "Evade potion"


class Store():
    def __init__(self, _hero):
        self._hero = _hero
        
        self.items = [
            Weapon('Bronze sword', 200000, 2, 1), # TODO POPULATE STORE WITH COOL SHIT
            Weapon('Iron sword', 4, 8, 2)
        ]
    
    def print_items(self):
        if self.items != []:
            print("Items for sale:")
            for item in self.items:
                print(f"\t{item.name} - costs {item.price} gold")
        else:
            print("The store has no items right now, come back later!")
    
    def buy(self):
        desired_item = input("What item would you like to buy?\n> ")
        for item in self.items:
            if item.name.lower() == desired_item:
                # hero gold checking
                if self._hero.gold < item.price:
                    print("You don't have enough money for that. Stop wasting my time, get out of my store! Shoo!")
                    return

                self._hero.gold -= item.price
                self._hero.inv.append(item)
                print(f"You bought the {item.name}.")
                print(f"you now have {self._hero.gold} gold")
                self.items.remove(item)
                break

        else:
            print("Sorry, we don't have that in stock. Make sure you entered the item name correctly")

    def sell(self, item):
        pass
    
    def go_shopping(self, _hero):
        # items = Items('Store')
        # MAYBE PRINT SOMETHING LIKE "Here is your current inventory:\n"
        self._hero.print_inventory()
        while True:
            print("""
                Welcome to the store
                ====================
                What do you want to do?
                1. List items for sale
                2. Buy item
                3. Sell item
                4. Exit Store
                """, end='\n> ')
            picker = int(input())
            if picker == 1:
                self.print_items()

            elif picker == 2:
                self.buy()

            elif picker == 3:
                pass

            elif picker == 4:
                print("\nThanks for visiting!")
                break

if __name__ == "__main__":

    tonic = SuperTonic("test", 69, "23")
    print(vars(tonic))
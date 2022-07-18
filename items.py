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

class Armor(Item):
    def __init__(self, name, price, defense, level, power):
        self.power = power
        self.level = level
        self.name = name
        self.price = price
        self.defense = defense
        self.equippable = False

    def use(self, _hero):
        _hero.armor += self.defense
        print(f"Enemies now do {self.defense} less damage to you")

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

    def use(self, _hero):
        if _hero.health == _hero.max_health:
            print("your health is already full!")
        else:
            _hero.health = _hero.max_health
            print(f"Your health has been restored to {_hero.max_health}.")
            _hero.inv.remove(self)
    
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
            Weapon('Iron sword', 200, 20, 2), # TODO POPULATE STORE WITH COOL STUFF
            Weapon('Bronze sword', 10, 5, 1),
            Armor('Iron Armor', 20, 2, 1, 0)
        ]
        
    def print_items(self):
        if self.items != []:
            print("Items for sale:")
            for item in self.items:
                if item.power > 0:
                    print(f"\t{item.name} - costs {item.price} gold and does {item.power} damage")
                else:
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
                print(f"You bought the {item.name}.")
                print(f"you now have {self._hero.gold} gold")

                if type(item).__name__ == "Armor":
                    item.use(self._hero)
                    break
                else:
                    self.items.remove(item)
                    self._hero.inv.append(item)
                    if item.equippable:
                        equip = input(f"Would you like to equip {item.name}? y/n\n>")
                        if equip.lower == 'yes' or 'y':
                            self._hero.equip(item)
                    break
        else:
            print("Sorry, we don't have that in stock. Make sure you entered the item name correctly")

    def sell(self, item):
        pass
    
    def go_shopping(self, _hero):
        self._hero.print_inventory()
        while True:
            picker = input("""
            Welcome to the store
            ====================
            What do you want to do?
            1. List items for sale
            2. Buy item
            9. Exit Store\n> """)
            if picker == '1':
                self.print_items()

            elif picker == '2':
                self.buy()

            elif picker == '3':
                pass

            elif picker == '9':
                print("\nThanks for visiting!")
                break
            else:
                print("That's not a valid option")

# if __name__ == "__main__":

#     tonic = SuperTonic("test", 69, "23")
#     print(vars(tonic))
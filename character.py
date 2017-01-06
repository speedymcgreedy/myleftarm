# Character class

import random

class Character():

    # initialize the character with their name.
    def __init__(self, name):
        self.__name=name    # player's input name.
        self.__health=51    # number of days player is alive initially.
        self.__inventory=['Street clothes'] # inventroy is empty initially.
        self.__hardInventory=[]  # items that cannot be lost easily
        self.__vision=2     # type and number of options available per room.
        self.__attack=1     # fists as weapon.
        self.__armor=3      # street clothes as armor.
        self.__room_count=0 # rooms completed
        self.__alien_count=0 # aliens defeated this game.

    def reset(self):
        # vision reset
        # Player cannot see anything if 'Blind'
        if 'Blind' in self.__hardInventory:
            self.__vision=0
        # 'Infection' of the eyes decreases vision.
        elif 'Infection' in self.__hardInventory:
            self.__vision=1
        # If eyes are healthy, then items can increase vision.
        # Vision is always maximized by best item.
        elif 'Flashlight' in self.__inventory:
            self.__vision=4
        elif 'Lamp' in self.__inventory:
            # 'Oil' increase vision from 'Lamp'.
            if 'Oil' in self.__inventory:
                self.__vision=4
            else:
                self.__vision=3
        else: # Normal vision
            self.__vision=2
        # attack reset
        # 'Handless' character cannot fight.
        if 'Handless' in self.__hardInventory:
            self.__attack=0
        # Best weapon is always equipped if not 'Handless'
        elif 'Old gun' in self.__inventory:
            misfire=random.randint(1,5) # 20% chance to misfire
            if misfire==1:
                self.__attack=1
            else:
                self.__attack=6
        elif 'Machete' in self.__inventory:
            self.__attack=5
        elif 'Brass knuckles' in self.__inventory:
            self.__attack=4
        elif 'Pocket knife' in self.__inventory:
            self.__attack=3
        elif 'Broom' in self.__inventory:
            self.__attack=2
        else:
            self.__attack=1
        # Naked means no armor.
        if 'Street clothes' not in self.__inventory:
            if 'Leather clothing' not in self.__inventory:
                self.__armor=0

    def reset_armor(self):
        if 'Leather clothing' in self.__inventory:
            self.__armor=5
        elif 'Street clothes' in self.__inventory:
            self.__armor=3
        else:
            self.__armor=0

    def reset_alien_count(self):
        self.__alien_count=0

    def lose_health(self):
        self.__health-=1
        print('Health decreased by 1!')

    def lose_ten_health():
        self.__health-=10
        print('Major damage!\nHealth decreased by 10!')

    def gain_health(self):
        self.__health+=1
        print('Health increased by 1!')

    def gain_item(self, item):
        self.__inventory.append(item)

    def lose_item(self, item):
        self.__inventory.remove(item)

    def lose_random_item(self):
        item=self.__inventory.pop()
        return item

    def gain_hard_item(self, item):
        self.__hardInventory.append(item)

    def lose_hard_item(self, item):
        self.__hardInventory.remove(item)

    def gain__vision(self):
        self.__vision+=1

    def lose_vision(self):
        self.__vision-=1

    def gain_attack(self):
        self.__attack+=1

    def lose_attack(self):
        self.__attack-=1

    def gain_armor(self):
        self.__armor+=1

    def lose_armor(self):
        self.__armor-=1
        if self.get_armor()==4:
            print('Your clothing took slight damage.')
        elif self.get_armor()==3:
            print('Your clothing took slight damage.')
        elif self.get_armor()==2:
            print('Your clothes have become worn from the fight.')
        elif self.get_armor()==1:
            print('Your clothes are starting to rip after that fight.')
        else:
            print('You clothes are all but strings now. You are naked!')
            if 'Street clothes' in self.get_inventory():
                self.lose_item('Street clothes')
            else:
                self.lose_item('Leather clothing')
    # Updates character on current room, inventory, and health.
    def new_room(self):
        self.__health-=1
        self.__room_count+=1
        print('Current Room: '+str(self.__room_count))
        print('Current Inventory: ', end='| ')
        for item in self.get_inventory():
            print(item, end=' | ')
        print('\nHealth: '+str(self.__health))
        if self.__health==2:
            print('LOW ON HEALTH!!!')
        if self.__health==1:
            print('Find health or this is your last room!!!')

    def kill_alien(self):
        self.__alien_count+=1
        
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_inventory(self):
        return self.__inventory

    def get_hardInventory(self):
        return self.__hardInventory

    def get_vision(self):
        return self.__vision

    def get_attack(self):
        return self.__attack

    def get_armor(self):
        return self.__armor

    def get_room_count(self):
        return self.__room_count

    def get_alien_count(self):
        return self.__alien_count

    def display_inventory(self):
        inv=''
        for item in self._inventory:
            inv+item+' | '
        return inv

    def __str__(self):
        inv=''
        for item in self.__inventory:
            inv+item+' | '
        return "Name: "+self.__name+\
        "\nHealth: " +str(self.__health)+\
        "\nInventory: "+''.join(self.__inventory)+\
        "\nInternal Inventory: "+''.join(self.__hardInventory)+\
        "\nAttack: "+str(self.__attack)+\
        "\nArmor: "+str(self.__armor)+\
        "\nRoom Count: "+str(self.__room_count)

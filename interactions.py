# interactions module

import random, time
import character
import introoutro

# Global constant for the list of items player can find.
ITEM=['Lamp', 'Broom', 'Pocket knife', 'Machete', 'Alcohol', 'Medicine', 'Oil', 'Lock','Leather clothing',\
          'Brass knuckles', 'Book', 'Spellbook', 'Flashlight', 'Old gun', 'Street clothes']

# chooseItem lets the player use an item or add it to their inventory that is in the room.
def chooseItem(player, items):
    if len(items)>0: # If there are items in the room.
        # Display the items in the room.
        print('You can see the following items lying in the room:')
        # Player can choose 1 item.
        num=len(items)
        for x in range(num):
            y=x+1
            print(y, ') ', sep='', end='')
            print(items[x])
        input('')
        print('Enter the number of the item you would like to pick up.')
        print('There is only time to get one! (Hit enter to leave the items)')
        playerItem=input('ITEM Number: ')
        print()
        if playerItem.isdigit()==True: # If player inputs integer.
            index=int(playerItem)-1 # Desired index is input-1
            if index>=0 and index<=num: # if index 0:len(items)
                pickupItem=items[index]
                evaluateItem(pickupItem, player)
            else:
                print('No item was retrieved.')
        else:
            print('No item was retrieved.')
        input()
    player.reset() # Update the player's stats with the new item.

# exploreFurniture lets the player interact with the room.
def exploreFurniture(player, furniture):
    if len(furniture)>0: # If the room contains furniture.
        # Display the rooms furniture.
        print('The room has furniture in it that you can interact with.')
        num=len(furniture)
        for x in range(num):
            y=x+1
            print(y, ') ', sep='', end='')
            print(furniture[x])
        input('')
        # Player can choose 1 to interact with.
        print('Enter the item of the furniture you would like to explore.')
        print('You can explore one of these, or press "Enter" to leave the room.')
        playerExplore=input('EXPLORE: ')
        if playerExplore.isdigit()==True: # If player inputs integer.
            index=int(playerExplore)-1 # Desired index is input-1
            if index>=0 and index<=num: # if index 0:len(items)
                explore=furniture[index]
                print()
                loadFurniture(player, explore)
            else:
                print('Nothing was explored.')
        else:
            print('Nothing was explored.')
    input()

# loadFurniture contains all the interactions the player can have with the furniture in a room.      
def loadFurniture(player, furniture):
    trap=random.randint(1,20) # 5% chance that some furniture will be trapped.
    deathTrap=False
    if trap==1: # If trap was 1 set the deathTrap
        deathTrap=True
    # The Bed allows the player to sleep.
    if furniture=='Bed':
        print('You are going to sleep for a while.')
        input()
        if deathTrap==True: # The deathtrap was in play.
            print('The Bed had a trap under the matress!\nIt ignites in flames after you laid down.')
            input()
            for x in range(25): # Player loses 25 health.
                player.lose_health()
            return
        else: # Bed is safe, pass player to sleeping()
            sleeping(player)
    # The Refridgerator can heal or infect the player.
    elif furniture=='Refridgerator':
        print('You open the fridge to get some nourishment in these harsh conditions.')
        print('******')
        input()
        risk=random.randint(1,2) # each outcome is 1:2
        if risk==1: # 50% to gain health
            print('Somehow there was still electricity, and it was full of food!')
            for x in range(2): # Gain 2 health.
                time.sleep(0.5)
                print('***nom***nom***nom***')
                player.gain_health()
                
        else: # 50% to get Infection.
            print('The fridge has been without power for months.')
            print('All of the spoiled food explodes onto you!.')
            input()
            print('***splooge***')
            input()
            print('As a result, your vision has decreased from an Infection.')
            input()
            infection(player) # pass player to infection()
            print('Try to locate something to clean your eyes with!')
    # The Sink can heal, damage, or infect
    elif furniture=='Sink':
        print('The water from the sink tastes potable!')
        input()
        risk=random.randint(1,3) # 1:3 chance per outcome
        if risk==1: # 33% chance to heal or remove Infection
            if 'Infection' in player.get_hardInventory(): # If Infection
                print('You use the water to clean out your eyes.')
                player.lose_hard_item('Infection') # Remove Infection
                print('Your vision was restored, but the sink is now dry.')
            else: # No Infection, heal player
                print('The water has refreshed you!')
                input()
                for x in range(2): # Gain 2 health
                    player.gain_health()
                    time.sleep(0.5)
        elif risk==2: # 33% chance at damage
            print("Your stomach starts turning, maybe it wasn't good?")
            input()
            for x in range(2): # Player loses 2 health
                player.lose_health()
                time.sleep(0.5)
            infect=random.randint(1,4) # 1:4 chance at Infection
            if infect==1: # 25% chance of Infection.
                print("Your eye's start burning from the water.\nYou shouldn't have washed your face in the sink!")
                input()
                print('As a result, your vision has decreased from an Infection.')
                input()
                infection(player) # Pass player to infection()
                print('Try to locate something to clean your eyes with!')
        else: # 33% chance sink was dry.
            print('Unfortunately there was only enough water to taste it. It is dry!')
    # The Bookshelf can give books or have deathTrap
    elif furniture=='Bookshelf':
        print('You look through the books in the Bookshelf')
        input()
        if deathTrap==True: # The deathtrap was in play.
            print('The Bookshelf had a trap behind it!\nUranimum was hidden behind one of the books.')
            input()
            for x in range(25): # Player loses 25 health
                print('***radiation***')
                player.lose_health()
            return
        bookType=random.randint(1,4) # Chances for the books, 25% each.
        if bookType==1: # No books, 25%
            print('All the books are wet and moldy.')
        elif bookType==2: # Spellbook, 25%
            print('You found a valuable Spellbook!')
            input()
            evaluateItem('Spellbook', player)
        else: # Book, 50%
            print('You found a common Book.')
            input()
            evaluateItem('Book', player)
    # Painting can have a secret compartment, wall, or deathTrap
    elif furniture=='Painting':
        print('You look behind the Painting.')
        print('***peeking***')
        input()
        if deathTrap==True: # The deathTrap was in play.
            print('The Painting had a trap behind it!\nA grenade exploded in your face.')
            input()
            for x in range(25): # Player loses 25 health
                player.lose_health()
            return
        find=random.randint(1,4) # Chances for secret compartment
        if find==1: # Find item, 25%
            item=random.choice(ITEM) # Random item from ITEM list
            print('Behind the painting was a secret compartment.\nIt contained '+item+'!')
            input()
            evaluateItem(item, player)
        elif find==2: # Empty compartment, 25%
            print('Behind the painting was a secret compartment.\nIt was empty!')
        else: # No compartment, 50%
            print('Behind the painting was just a wall.')
    # The Grill can heal player if Oil in the inventory.
    elif furniture=='Grill' and 'Oil' in player.get_inventory():
        print('You use your Oil with the grill to cook some meat you had!')
        player.lose_item('Oil') # Remove Oil from the inventory.
        print('You hunger is gone, you feel healthy!')
        input()
        for x in range(2): # Gain 2 Health.
            player.gain_health()
            time.sleep(0.5)
    # The Fireplace can heal player if Oil in the inventory.
    elif furniture=='Fireplace' and 'Oil' in player.get_inventory():
        print('You use your Oil to start a fire. \nNow you can sleep in its warmth!')
        player.lose_item('Oil') # Remove Oil from the inventory.
        input()
        print('The fire should keep enemies at bay while you sleep.')
        for x in range(3):
            print('ZZZ ZZZ ZZZ')
            time.sleep(0.5)
        print('\nYou feel well rested now!')
        input()
        for x in range(2): # Gain 2 Health.
            player.gain_health()
            time.sleep(0.5)
    # All other furniture has items, nothing, or a deathTrap
    else:
        print('You begin looking around the ', furniture, '.', sep='')
        print('***rummage***rummage***rummage***')
        input()
        if deathTrap==True: # The Deathtrap was in play.
            print('The', furniture, 'was trapped!\nAcid squirted all over your body.')
            input()
            for x in range(25): # Player loses 25 health
                player.lose_health()
            return
        find=random.randint(1,3) # Odds to find item, 1:3
        if find==1: # Find item, 33%
            item=random.choice(ITEM) # Random item from ITEM list
            print('After looking around you have found ', item, '.', sep='')
            input()
            evaluateItem(item, player)
        else: # Find nothing, 66%
            print('There is nothing usable here.')
    player.reset() # Update player's stats with any new items.

# itemInteraction uses items on the player that must be used imidiately upon gaining.
def itemInteraction(player, item):
    if item=='Medicine': # Medicine can heal your wounds.
        print('You used the Medicine on your wounds.')
        for x in range(2): # Player gains 2 health.
            time.sleep(0.5)
            player.gain_health()
    elif item=='Alcohol': # Alcohol will remove Infection or make you sleep.
        if 'Infection' in player.get_hardInventory(): # Remove Infection.
            print('You use the alcohol to treat your eye infection.\nVISION RESTORED!')
            player.lose_hard_item('Infection')
        else: # Pass player to sleeping()
            print('The alcohol tasted good but made you pass out!')
            sleeping(player)

# sleeping() will heal, harm, or make the player lose items.
def sleeping(player):
    for x in range(3):
        print('ZZZ ZZZ ZZZ')
        time.sleep(0.5)
    risk=random.randint(1,4) # Chances for each outcome.
    if risk==1: # Player gets robbed and healed, 25%
        print('\nYOU WERE ROBBED IN YOUR SLEEP!')
        input()
        stolen=player.lose_random_item() # Thief takes random item.
        print('The thief has taken your ', stolen, '.', sep='')
        print('At least you feel well rested though!')
        input()
        for x in range(2): # Player gains 2 health.
            time.sleep(0.5)
            player.gain_health()
    elif risk==2: # Player gets attacked while sleeping, 25%
        print('\nYou wake up to an assailant attacking you!')
        input()
        print('In your groggy state, you cannot fight back...')
        for x in range(2): # Player loses 2 health.
            time.sleep(0.5)
            player.lose_health()
    else: # Player is healed, 50%
        print('\nYou feel well rested now!')
        input()
        for x in range(2): # Player gains 2 health.
            time.sleep(0.5)
            player.gain_health()

# infection() adds Infection or Blind to the player's invetory. May end game.
def infection(player):
    # Player was already infected and becomes Blind.
    if 'Infection' in player.get_hardInventory():
        print('You already had infected eyes.\nYOU WENT BLIND!')
        player.gain_hard_item('Blind') # Add Blind to inventory.
        input()
        print('You can there is no chance of survival now.')
        input()
        introoutro.endgame(player) # Player loses.
    else: # Player becomes infected.
        player.gain_hard_item('Infection')

# loot() allows the player to gain a random item from the ITEM list.
def loot(player):
    print('You loot your opponent.')
    item=random.choice(ITEM) # item is a random item from ITEM
    print('You have stolen  ', item, '.', sep='')
    input()
    evaluateItem(item, player)

def evaluateItem(item, player):
    if item=='Leather clothing':
        print('You got some new clothes!')
        if 'Leather clothing' not in player.get_inventory():
            player.gain_item(item)
            player.reset_armor()
        if  'Street clothes' in player.get_inventory():
            print('These are more sturdy than the clothes you had')
            player.lose_item('Street clothes')
    elif item=='Street clothes' and 'Leather clothing' not in player.get_inventory():
        print('You got some new clothes!')
        if 'Street clothes' not in player.get_inventory():
            player.gain_item(item)
        player.reset_armor()
    elif item=='Street clothes' and 'Leather clothing' in player.get_inventory():
        print('These clothes are not as sturdy as the ones you are wearing!')
        if player.get_armor()<3:
            print('You used the Street clothes to repair your Leather clothing.')
            while player.get_armor()<3:
                player.gain_armor()
    else:
        # Use Medicine or Alcohol immidiately.
        if item=='Medicine' or item=='Alcohol':
            itemInteraction(player, item)
        elif item in player.get_inventory():
            print('You already have one of those!')
            print('Carrying more would weigh you down.')
        # Add anything else to the inventory.
        else:
            player.gain_item(item)
            print(item, 'added to your inventory!')
            player.reset()

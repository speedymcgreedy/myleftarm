# rooms module

import random
import character
import interactions, altercations

# Global constants for the list of interactables
FURNITURE=['Chair', 'Table', 'Bookshelf', 'Bed', 'Sink', 'Computer', \
               'Television', 'VCR', 'Refridgerator', 'Painting', 'Grill', 'Fireplace']
ITEM=['Lamp', 'Broom', 'Pocket knife', 'Machete', 'Alcohol', 'Medicine', 'Oil', 'Lock','Leather clothing',\
          'Brass knuckles', 'Book', 'Spellbook', 'Flashlight', 'Old gun', 'Street clothes']
NPC=['Thief', 'Bandit', 'Brawler', 'Mutant', 'Murderer', 'Nurse', 'Alcoholic', 'Magician']
MONSTER=['Spider', 'Wolfpack', 'Group of Mice', 'Bear', 'Alien']
BFG='MLA'

def generateRoom(player):
    room=[] # room starts out empty
    for x in range(2): # Fill the room up twice
        # Different weightings depending on vision.
        if player.get_vision()==1: # 2 monsters from less light
            room.append(random.choice(FURNITURE))
            room.append(random.choice(ITEM))
            room.append(random.choice(NPC))
            for x in range(2):
                room.append(random.choice(MONSTER))
        elif player.get_vision()==2: # 1 of all
            room.append(random.choice(FURNITURE))
            room.append(random.choice(ITEM))
            room.append(random.choice(NPC))
            room.append(random.choice(MONSTER))
        elif player.get_vision()==3: # 2 furniture from more light
            for x in range(2):
                room.append(random.choice(FURNITURE))
            room.append(random.choice(ITEM))
            room.append(random.choice(NPC))
            room.append(random.choice(MONSTER))
        elif player.get_vision()==4: # 2 npc and furniture from max light
            for x in range(2):
                room.append(random.choice(FURNITURE))
                room.append(random.choice(NPC))
            room.append(random.choice(ITEM))
            room.append(random.choice(MONSTER))
    roomAttributes=[] # roomAttributes are what player can interact with.
    if player.get_room_count()==20:
        player.gain_hard_item(BFG)
    random.shuffle(room) # shuffle the room
    # add the first 3 or 4 things from the room to the roomAttributes based on vision
    if player.get_vision()<=2: 
        for x in range(3): 
            roomAttributes.append(room[x])
    else:
        for x in range(4):
            roomAttributes.append(room[x])
    return roomAttributes

def enterRoom(player, room):
    # Empty list for monsters, npcs, items, and furniture in the room.
    monsters=[]
    npcs=[]
    items=[]
    furniture=[]
    # Sort each attribute of the room into one of the previous lists based on the Global variables.
    for attribute in room:
        if attribute in MONSTER:
            monsters.append(attribute)
        elif attribute in NPC:
            npcs.append(attribute)
        elif attribute in ITEM:
            items.append(attribute)
        else:
            furniture.append(attribute)
    # If there are monsters and npcs in the room.
    if len(monsters)>0 and len(npcs)>0:
        if len(monsters)==len(npcs): # If the room has equal amounts of monsters and npcs.
            status='triple' 
            monster=monsters[0]
            npc=npcs[0]
            fight=altercations.intervene(monsters) # Player decides on intervention in monster/npc fight.
            if fight==True:
                win=altercations.fightMonster(player, monster, status) # If player saves npc.
                if win==True:
                    win2=altercations.engageNPC(player, npc, status) # If npc was friendly to player.
                    if win2==True:
                        interactions.exploreFurniture(player, furniture) # Explore furniture
            else: # Player leaves room.
                print('You cowardly abandon the victim to the '+monster+'.')
                input()
        elif len(monsters)>len(npcs): # If more monsters than npcs.
            status='double'
            monster=monsters[1] # monster is the second entry in the monsters list.
            altercations.dueling(npcs, monsters) # Display who is fighting.
            win=altercations.fightMonster(player, monster, status) # Fight the monster, leave room.
        else: # If more npcs than monsters.
            status='double'
            npc=npcs[1] # npc is the second entry in the npcs list.
            altercations.dueling(npcs, monsters) # Display who is fighint.
            win=altercations.engageNPC(player, npc, status) # Engage the npc, leave room.
    # If no npcs in the room.
    elif len(monsters)>0:
        status='single'
        monster=monsters[0] # monster is the first monster in the monsters list.
        interactions.chooseItem(player, items) # Look for items
        player.reset() # Update player with new item before monster fight.
        win=altercations.fightMonster(player, monster, status) # Fight monster.
        if win==True and len(furniture)>0: # explore the room if there is furniture and beat monster.
            interactions.exploreFurniture(player, furniture)
    # If no monsters in the room.
    elif len(npcs)>0:
        status='single'
        npc=npcs[0] # npc is the first npc in the npcs list.
        win=altercations.engageNPC(player, npc, status) # Engage with the npc
        if win==True and len(furniture)>0: # explore the room if there is furniture and npc did not defeat player.
            interactions.exploreFurniture(player, furniture)
    # If no monsters or npcs
    else:
        print('There appears to be nothing alive in this room.')
        input()
        interactions.chooseItem(player, items) # Look for items
        interactions.exploreFurniture(player, furniture) # Explore the room.
    print('You leave the room.')
    input()

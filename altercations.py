# altercat module.
 dfdfd
import random, time
import character
import interactions, characters

# engageNPC() will take the player, npc, and status of interaction.
# The player and status are then passed to the correct npc function.
# Win status from the npc function is returned.
def engageNPC(player, npc, status):
    if npc=='Thief':
        win=characters.thief(player, status)
    elif npc=='Bandit':
        win=characters.bandit(player, status)
    elif npc=='Brawler':
        win=characters.brawler(player, status)
    elif npc=='Mutant':
        win=characters.mutant(player, status)
    elif npc=='Murderer':
        win=characters.mutant(player, status)
    elif npc=='Nurse':
        win=characters.nurse(player, status)
    elif npc=='Alcoholic':
        win=characters.alcoholic(player, status)
    else:
        win=characters.magician(player, status)
    player.reset() # Update player stats after npc interaction.
    return win # Return win status.

# fightMonster() will take the player, monster, and status of interaction.
# The player and status are then passed to the correct monster function.
# Win status from the monster function is returned.
def fightMonster(player, monster, status):
    if monster=='Group of Mice':
        win=characters.groupOfMice(player, status)
    elif monster=='Wolfpack':
        win=characters.wolfpack(player, status)
    elif monster=='Spider':
        win=characters.spider(player, status)
    elif monster=='Bear':
        win=characters.bear(player, status)
    else:
        win=characters.alien(player, status)
    player.reset() # Update player stats after monster fight.
    return win # Return win status.

# dueling() will take two lists and display the first index of each list as fighting.
def dueling(npcs, monsters):
    npc=npcs[0]
    monster=monsters[0]
    if npc=='Alcoholic' and monster=='Alien':
        print('You enter the room to see an '+npc+' fighting with an '+monster+'.')
    elif npc=='Alcoholic':
        print('You enter the room to see an '+npc+' fighting with a '+monster+'.')
    elif npc=='Alien':
        print('You enter the room to see a '+npc+' fighting with an '+monster+'.')
    else:
        print('You enter the room to see a '+npc+' fighting with a '+monster+'.')
    input()
    
# intervene() takes a list of monsters and displays that the monster is attacking someone.
# The player chooses to attack the monster or not. The choice is returned.
def intervene(monsters):
    monster=monsters[0]
    if monster=='Alien':
        print('You enter the room to see an Alien attacking someone!')
    else:
        print('You enter the room to see a '+monster+' attacking someone!')
    input()
    print('Would you like to stop the monster?')
    attack=input('(Yes or No): ')
    print()
    if attack.lower()=='yes' or attack.lower()=='y':
        return True
    else:
        return False

# enemyCounter will check if the character has killed a set amount of monsters
# to initiate a Boss battle. A boss or False is returned.
def counters(player):
    if player.get_room_count()==30:
        boss='Overseer'
    elif player.get_room_count()==50:
        boss='Final Overseer'
    #elif player.get_alien_count()==10:
        #boss='Alien Overlord'
        #player.reset_alien_count()
    else:
        boss=False
    return boss

def fightBoss(player, boss):
    if boss=='Overseer':
        characters.overseer(player)
    elif boss=='Final Overseer':
        characters.finalOverseer(player)
    # Alien Overlord is currently in production phase
    #elif boss=='Alien Overlord':
        #alienOverlord(player)
        
        

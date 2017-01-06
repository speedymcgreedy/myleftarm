# myleftarm game
# 1,177 lines
# written by speedymcgreedy

import character
import introoutro, rooms, altercations

def main():
    introoutro.intro() # Introduction to the game.
    name=input('What is your name? ') # Player enters their name
    player=character.Character(name) # create a Character from the name.
    print()
    while player.get_health()>1:   # while player still has health keep playing.
        player.reset()# reset player based on current inventory items.
        print('You enter a new room.\n')
        player.new_room() # increase room + decrease health
        input()
        boss=altercations.counters(player)
        if boss!=False:
            altercations.fightBoss(player, boss)
        else:
            room=rooms.generateRoom(player) # room is a list of the random contents. of a room
            #print(room) #####DEBUGGING#####
            rooms.enterRoom(player, room) # player enters the room.
    introoutro.endgame(player)

# Call the main function.
main()

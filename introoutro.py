# introduction and endgame stuffs

import pickle, time, sys
import character

def intro():
    print('(Intro to the game goes here)')

def endgame(player):
    endingFile(player)
    print('(Ending goes here)')
    # Display the player's ending inventory and rooms
    print('\nFinal attributes for '+player.get_name()+'.')
    print('-----------------------------------------------------------')
    print('Inventory: ', end='| ')
    s=0
    if len(player.get_inventory())>0:
        for item in player.get_inventory():
            x+=1
            print(item, end=' | ')
            if x%5==0:
                print('\n           ', end='| ')
    if len(player.get_hardInventory())>0:
        for item in player.get_hardInventory():
            x+=1
            print(item, end=' | ')
            if x%5==0:
                print('\n           ', end='| ')
    print('\nRooms Completed: '+str(player.get_room_count()))
    print('\n\n\nPress enter to exit.')
    input() # User hits 'Enter' to quit.
    sys.exit() # Exit the game.

def endingFile(player):
    filename='player.dat' # Save file.
    try:
        inFile=open(filename, 'rb')
        savedGames=pickle.load(inFile)
        inFile.close()
    except IOError:
        savedGames=[]
    print(savedGames)
    savedGames.append(player)
    print(savedGames)
    try: # Save the player instance to binary
        outFile=open(filename, 'wb')
        pickle.dump(savedGames, outFile)
        outFile.close()
        return
    except IOError: # If the game did not save for some reason, give option to email.
        print('Your game did not save, sorry bra... :(')
        print('Printscreen in ten seconds and send that in as your proof!')
        time.sleep(10)
        return

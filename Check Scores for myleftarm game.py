import character
import pickle

def main():
    filename='player.dat'
    inFile=open(filename, 'rb')
    savedGames=pickle.load(inFile)
    inFile.close()
    for player in savedGames:
        score=character.Character(player)
        print(player)
        print()
    input()
main()

import os
import sys

clear = lambda: os.system('cls')

def getPlayerInput(player):
    currentLocat = player.locat
    print()
    playerCmd = input('Select an Action:')

    for idx, val in enumerate(currentLocat.getActions(), start=1):
        if playerCmd == str(idx):
            if "North" in str(val):
                player.locat = currentLocat.n_to
                clear()
                print(currentLocat.n_journey)
            if "East" in str(val):
                player.locat = currentLocat.e_to
                clear()
                print(currentLocat.e_journey)
            if "South" in str(val):
                player.locat = currentLocat.s_to
                clear()
                print(currentLocat.s_journey)
            if "West" in str(val):
                player.locat = currentLocat.w_to
                clear()
                print(currentLocat.w_journey)
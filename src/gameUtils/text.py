import os
import sys
from .playerInput import getPlayerInput


clear = lambda: os.system('cls')

def gap():
    print()
    print()

def printUI():
    gap()
    print('Actions:')

def venture(player):
    player.locat.actions = []

    for idx, val in enumerate(player.locat.getActions(), start=1):
        print(f"[{idx}]: {val}")

    getPlayerInput(player)

def explore(player):
    print('[1] Look around.')
    print()
    playerCmd = input('Select an Action:')

    if playerCmd == 'QUIT':
        gameOver = True
        print('oof... Game Over...')

    if playerCmd == '1':
        player.locat.explored == True
        describe(player)

def describe(player):
    clear()
    print("You look around...")
    print(player.locat.desc)
    gap()
    print('Actions:')
    venture(player)


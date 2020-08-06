from .player import Player
from .room import Room
import os
import sys

clear = lambda: os.system('cls')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "South of you, the mouth of a narrow cave passage beckons.\nAll other directions only reveal steep drop offs into jagged cliffside.\nLooking from the treacherous ledges you can't manage to make out how high up you are.\nA thick and endless fog shrouds the distant lands below."),

    'foyer':    Room("Foyer",
                    "The cavern is covered with large pillars of stone and a small body of water bubbles in the center of the room.\nIt's hard to see but you can hear the howling of wind from the narrow entrance to the south and flickering orange lights reveal a wide passage to your north and a small dusty passage to your east."),

    'overlook': Room("Grand Overlook", 
                    "A steep cliff appears before you, falling into the darkness.\nAhead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", 
                    "The narrow passage bends here from west to north.\nThe smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", 
                    "You've found the long-lost treasure chamber!\nSadly, it has already been completely emptied by earlier adventurers.\nThe only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].n_journey = 'You make your way into the small cave passage.\nStrafing sideways to pass through it your shoulder blades slide across the cold stone wall and the howling winds of the cliffside begin to quiet.\nEventually the cave begins to open up and you find yourself in a small cavern.'

room['foyer'].s_to = room['outside']
room['foyer'].s_journey = 'You travel south and arrive at your destination.'

room['foyer'].n_to = room['overlook']
room['foyer'].n_journey = 'You travel north and arrive at your destination.'

room['foyer'].e_to = room['narrow']
room['foyer'].e_journey = 'Making your way through the dusty passage you tread eastward and stop when you begin to smell a strange scent.'

room['overlook'].s_to = room['foyer']
room['overlook'].s_journey = 'You travel south and arrive at your destination.'

room['narrow'].w_to = room['foyer']
room['narrow'].w_journey = 'You travel west and arrive at your destination.'

room['narrow'].n_to = room['treasure']
room['narrow'].n_journey = 'Heading towards the strange scent you spot a bright light at the end of the tunnel.\n You pass into it and shield your eys as they adjust.1'

room['treasure'].s_to = room['narrow']
room['treasure'].s_journey = 'You travel south and arrive at your destination.'

player = Player('defaultName', room['outside'])

def createPlayer(player):
    clear()
    while player.name == 'defaultName':
        playerName = input('What is your name Adventurer? ')
        player.name = playerName

def introText(player):
    clear()
    print(f'{player.name}, you have awoken on the edge of a towering cliffside.\nYou aren\'t quite sure how you got here and your memory is quite hazy.\nRunning your fingers across the back of your throbbing skull you are greeted with a stinging pain and the discovery of an open wound. ')

def run():
    createPlayer(player)
    introText(player)
    return player
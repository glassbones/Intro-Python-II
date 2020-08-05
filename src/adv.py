from room import Room
from player import Player
import os

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


#
# Main
#
clear = lambda: os.system('cls')


print(room['outside'].name)


def gap():
    print()
    print()

def createPlayer(player):
    clear()
    while player.name == 'defaultName':
        playerName = input('What is your name Adventurer? ')
        player.name = playerName

def introText(player):
    clear()
    print(f'{player.name}, you have awoken on the edge of a towering cliffside.\nYou aren\'t quite sure how you got here and your memory is quite hazy.\nRunning your fingers across the back of your throbbing skull you are greeted with a stinging pain and the discovery of an open wound. ')

def describeText(player):
    clear()
    print("You look around...")
    print(player.locat.desc)
    gap()
    print('Actions:')
    ventureText(player)

def ventureText(player):
    player.locat.actions = []

    for idx, val in enumerate(player.locat.getActions(), start=1):
        print(f"[{idx}]: {val}")

    getPlayerInput(player)

def exploreText(player):
    
    print('[1] Look around.')
    print()
    playerCmd = input('Select an Action:')

    if playerCmd == 'QUIT':
        gameOver = True
        print('oof... Game Over...')
    if playerCmd == '1':
        player.locat.explored == True
        describeText(player)
        

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

####################################################################################################################
####################################################################################################################
####################################################################################################################               
####################################################################################################################
####################################################################################################################
####################################################################################################################
def play():
    #init values
    gameOver = False
    player = Player('defaultName', room['outside'])
    
    #create player
    createPlayer(player)

    #start adventure
    introText(player)

    #game loop
    while not gameOver:

        gap()
        print('Actions:')

        if player.locat.explored:
            ventureText(player)
        else:
            exploreText(player)
        




play()
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

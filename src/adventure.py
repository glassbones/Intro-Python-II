import gameData.intro
import gameUtils.text as txt


def play():
    #init
    gameOver = False
    player = gameData.intro.run()
    #game loop
    while not gameOver:
        txt.printUI()
        if player.locat.explored:
            txt.venture(player)
        else:
            txt.explore(player)
play()


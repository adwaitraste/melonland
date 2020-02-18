# This file (start.py) is to be run to start the game

# Import self written classes
from player import Player
from level import Level

# Import config file
from config import GlobalSettings
gs = GlobalSettings()

# Import pygame libraries
import pygame

# Setup of game window
pygame.init()
win = pygame.display.set_mode((gs.screenWidth, gs.screenHeight))
pygame.display.set_caption(gs.title)

# Initialise fonts
font1 = pygame.font.Font(gs.font, gs.yFactor)
font2 = pygame.font.Font(gs.font, gs.yFactor//3)

# All start screen messages
startScreenMsg1 = font1.render(gs.startScreenMsg1, True, gs.red)
startScreenMsg1Rect = startScreenMsg1.get_rect()
startScreenMsg1Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 - 3*gs.yFactor
)

startScreenMsg2 = font2.render(gs.startScreenMsg2, True, gs.black)
startScreenMsg2Rect = startScreenMsg2.get_rect()
startScreenMsg2Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 + 3*gs.yFactor
)

startScreenMsg3 = font2.render(gs.startScreenMsg3, True, gs.black)
startScreenMsg3Rect = startScreenMsg3.get_rect()
startScreenMsg3Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 - 1*gs.yFactor
)

startScreenMsg4 = font2.render(gs.startScreenMsg4, True, gs.black)
startScreenMsg4Rect = startScreenMsg4.get_rect()
startScreenMsg4Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 - 0*gs.yFactor
)

startScreenMsg5 = font2.render(gs.startScreenMsg5, True, gs.black)
startScreenMsg5Rect = startScreenMsg5.get_rect()
startScreenMsg5Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 + 1*gs.yFactor
)


# Start Screen
startScreen = True
while startScreen:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startScreen = False

    # Draw on start screen
    pygame.draw.rect(win, gs.green, (0, 0, gs.screenWidth, gs.screenHeight)) 
    win.blit(startScreenMsg1, startScreenMsg1Rect) 
    win.blit(startScreenMsg2, startScreenMsg2Rect)
    win.blit(startScreenMsg3, startScreenMsg3Rect) 
    win.blit(startScreenMsg4, startScreenMsg4Rect)
    win.blit(startScreenMsg5, startScreenMsg5Rect)
    pygame.display.update()       


players = []        # Array to store players
players.append(Player(win, 0, 0, 1))
players.append(Player(win, 0, 0, 2))

# Run no of levels for each player
for i in range(1, gs.noOfLvls + 1):
    lvl = Level(i, win, players)
    lvl.playForPlayer1()


# All end screen messages
endScreenMsg1 = font1.render(gs.endScreenMsg1, True, gs.red)
endScreenMsg1Rect = endScreenMsg1.get_rect()
endScreenMsg1Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 - 3*gs.yFactor
)

endScreenMsg2 = font2.render(gs.endScreenMsg2, True, gs.black)
endScreenMsg2Rect = endScreenMsg2.get_rect()
endScreenMsg2Rect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 + 2*gs.yFactor
)

p1ScoreMsgTemp = "Player 1 Score: " + str(players[0].score)
p1ScoreMsg = font2.render(p1ScoreMsgTemp, True, gs.black)
p1ScoreMsgRect = p1ScoreMsg.get_rect()
p1ScoreMsgRect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 - 2*gs.yFactor
)

p2ScoreMsgTemp = "Player 2 Score: " + str(players[1].score)
p2ScoreMsg = font2.render(p2ScoreMsgTemp, True, gs.black)
p2ScoreMsgRect = p2ScoreMsg.get_rect()
p2ScoreMsgRect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2 + -1*gs.yFactor
)

if(players[0].score == players[1].score):
    winnerMsgTemp = "Its a Tie! Both players win"
elif(players[0].score > players[1].score):
    winnerMsgTemp = "Player 1 Wins!"
else:
    winnerMsgTemp = "Player 2 Wins!"
winnerMsg = font2.render(winnerMsgTemp, True, gs.red)
winnerMsgRect = winnerMsg.get_rect()
winnerMsgRect.center = (
    gs.screenWidth//2, 
    gs.screenHeight//2
)

# End screen 
endScreen = True
while endScreen:
    pygame.time.delay(10)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                endScreen = False

    # Draw on end screen
    pygame.draw.rect(win, gs.green, (0, 0, gs.screenWidth, gs.screenHeight))  
    win.blit(endScreenMsg1, endScreenMsg1Rect)
    win.blit(p1ScoreMsg, p1ScoreMsgRect) 
    win.blit(p2ScoreMsg, p2ScoreMsgRect)
    win.blit(winnerMsg, winnerMsgRect)
    win.blit(endScreenMsg2, endScreenMsg2Rect)
    pygame.display.update()     

pygame.quit()
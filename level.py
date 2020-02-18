# Class for level implementation

# Import python and pygame libraries
import pygame
import random
import time

# Import self written classes
from player import Player
from movingObstacle import MovingObstacle
from fixedObstacle import FixedObstacle

# Import config file
from config import GlobalSettings
gs = GlobalSettings()

# Load background images
ground = pygame.image.load(gs.groundImage)
ground = pygame.transform.scale(ground, (gs.xFactor, gs.yFactor))
water = pygame.image.load(gs.waterImage)
water = pygame.transform.scale(water, (gs.xFactor, gs.yFactor))


class Level():
    def __init__(self, lvl, win, players):
        self.win = win
        self.lvl = lvl
        self.movingObstacles = []
        self.fixedObstacles = []
        self.players = players

        # Initialise fonts
        self.font1 = pygame.font.Font(gs.font, gs.yFactor//3)
        self.font2 = pygame.font.Font(gs.font, gs.yFactor//2)

        self.diff = self.lvl + 1

    # Function to create obstacles as per difficulty level
    def createObstacles(self):
        for i in range(gs.rows - 1):
            i += 1
            if i % 2 == 0:
                for j in range(self.diff):
                    self.fixedObstacles.append(
                        FixedObstacle(
                            self.win,
                            i,
                            random.randint(0, gs.cols)
                        )
                    )
            else:
                for j in range(self.diff):
                    self.movingObstacles.append(
                        MovingObstacle(
                            self.win,
                            i,
                            random.randint(0, gs.cols),
                            random.randint(0, 1),
                            self.diff
                        )
                    )

    # Initialise obstacle arrays to null
    def destroyObstacles(self):
        self.movingObstacles = []
        self.fixedObstacles = []

    # Function called when players are to be switched ingame
    def switchPlayersMsg(self, status, score):
        run = True
        timeCounter = 0
        if(status):
            msg1 = self.font2.render(gs.successMsg, True, gs.green)
        else:
            msg1 = self.font2.render(gs.collidedMsg, True, gs.red)
        msg2 = self.font2.render(gs.switchPlayerMsg, True, gs.black)
        scrMsgTemp = "Your score: " + str(score)
        scrMsg = self.font2.render(scrMsgTemp, True, gs.black)
        scrMsgRect = scrMsg.get_rect()
        scrMsgRect.center = (gs.screenWidth//2, gs.screenHeight//2 + 10)
        msg1Rect = msg1.get_rect()
        msg1Rect.center = (gs.screenWidth//2, gs.screenHeight//2 - gs.yFactor)
        msg2Rect = msg2.get_rect()
        msg2Rect.center = (gs.screenWidth//2, gs.screenHeight//2 + gs.yFactor)

        while run:
            pygame.time.delay(10)
            timeCounter += 1
            if(timeCounter == 200):     # Keep screen for 2 seconds
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.draw.rect(
                self.win,
                gs.white,
                (0, 0, gs.screenWidth, gs.screenHeight)
            )
            self.win.blit(msg1, msg1Rect)
            self.win.blit(msg2, msg2Rect)
            self.win.blit(scrMsg, scrMsgRect)
            pygame.display.update()

    # Function to draw background
    def drawBackground(self):
        for i in range(gs.rows+1):
            if (i % 2 == 0):    # All even rows are ground rows
                for j in range(0, gs.cols+1):
                    self.win.blit(ground, (gs.xFactor*j, gs.yFactor*i))
                    pygame.draw.rect(
                        self.win,
                        gs.black,
                        (
                            gs.xFactor*j,
                            gs.yFactor*i,
                            gs.xFactor,
                            gs.yFactor
                        ),
                        1
                    )
            else:               # All odd rows are water rows
                for j in range(0, gs.cols+1):
                    self.win.blit(water, (gs.xFactor*j, gs.yFactor*i))
        i += 1

        # Last row is for showing player scores
        pygame.draw.rect(
            self.win,
            gs.green,
            (
                0,
                i * gs.yFactor,
                gs.screenWidth,
                gs.screenHeight
            )
        )

    # Play function for player 1
    def playForPlayer1(self):

        # Getting all texts related to player 1
        temp = "Level: " + str(self.lvl)
        playerText = self.font1.render("Player 1", True, gs.black)
        lvlText = self.font1.render(temp, True, gs.black)

        # Setting intial parameters for player 1
        p1 = self.players[0]
        p1.gridX = gs.xFactor*(gs.cols//2)
        p1.x = gs.xFactor*(gs.cols//2) + (gs.xFactor/2) - (p1.width/2)
        p1.gridY = gs.yFactor*gs.rows
        p1.y = gs.yFactor*gs.rows + (gs.yFactor/2) - (p1.height/2)

        self.createObstacles()

        p1Playing = True
        timeCounter = 0
        status = 0
        while p1Playing:
            pygame.time.delay(10)
            timeCounter += 1
            if(timeCounter == 50):      # Approximately occurs every second
                p1.score -= gs.timePenalty
                timeCounter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Movement controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if p1.x > gs.xFactor:
                            p1.move("left")
                    if event.key == pygame.K_RIGHT:
                        if p1.x < gs.cols*gs.xFactor:
                            p1.move("right")
                    if event.key == pygame.K_UP:
                        if p1.y > gs.yFactor:
                            p1.move("up")
                    if event.key == pygame.K_DOWN:
                        if p1.y < gs.rows*gs.yFactor:
                            p1.move("down")

            self.drawBackground()

            # Compute, Update and Display obstacles
            for mobs in self.movingObstacles:
                if p1.isCollided(mobs):
                    p1Playing = False
                    p1.score -= gs.dyingPenalty
                    status = 0
                mobs.checkOnEdge()
                mobs.move()
                mobs.draw()

            for fobs in self.fixedObstacles:
                if p1.isCollided(fobs):
                    p1Playing = False
                    p1.score -= gs.dyingPenalty
                    status = 0
                fobs.draw()

            # Get score text
            scrTextTemp = "Score: " + str(p1.score)
            scrText = self.font1.render(scrTextTemp, True, gs.black)

            # Display player and all texts
            p1.draw()
            self.win.blit(playerText, (0, gs.yFactor*(gs.rows+1)))
            self.win.blit(lvlText, (0, gs.yFactor*(gs.rows+1.5)))
            self.win.blit(
                scrText,
                (gs.xFactor*(gs.cols//2), gs.yFactor*(gs.rows+1))
            )

            # If player 1 reaches his finish
            if p1.y < gs.yFactor:
                p1Playing = False
                status = 1
                p1.score += gs.completeScore    # Bonus points for completion

            pygame.display.update()

        time.sleep(0.5)     # 0.5 second gap
        self.switchPlayersMsg(status, p1.score)
        self.destroyObstacles()
        self.playForPlayer2()       # Player 2 plays after player 1

    # Play function for player 2
    def playForPlayer2(self):

        # Getting all texts related to player 2
        temp = "Level: " + str(self.lvl)
        playerText = self.font1.render("Player 2", True, gs.black)
        lvlText = self.font1.render(temp, True, gs.black)

        # Setting intial parameters for player 2
        p2 = self.players[1]
        p2.x = gs.xFactor*(gs.cols//2) + (gs.xFactor/2) - (p2.width/2)
        p2.y = 0 + (gs.yFactor/2) - (p2.height/2)

        self.createObstacles()

        p2Playing = True
        timeCounter = 0
        status = 0
        while p2Playing:
            pygame.time.delay(10)
            timeCounter += 1
            if(timeCounter == 50):      # Approximately occurs every second
                p2.score -= gs.timePenalty
                timeCounter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Movement controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if p2.x > gs.xFactor:
                            p2.move("left")
                    if event.key == pygame.K_RIGHT:
                        if p2.x < gs.cols*gs.xFactor:
                            p2.move("right")
                    if event.key == pygame.K_UP:
                        if p2.y > gs.yFactor:
                            p2.move("up")
                    if event.key == pygame.K_DOWN:
                        if p2.y < gs.rows*gs.yFactor:
                            p2.move("down")

            self.drawBackground()

            # Compute, Update and Display obstacles
            for mobs in self.movingObstacles:
                if p2.isCollided(mobs):
                    p2Playing = False
                    p2.score -= gs.dyingPenalty
                    status = 0
                mobs.checkOnEdge()
                mobs.move()
                mobs.draw()

            for fobs in self.fixedObstacles:
                if p2.isCollided(fobs):
                    p2Playing = False
                    p2.score -= gs.dyingPenalty
                    status = 0
                fobs.draw()

            # Get score text
            scrTextTemp = "Score: " + str(p2.score)
            scrText = self.font1.render(scrTextTemp, True, gs.black)

            # Display player and all texts
            p2.draw()
            self.win.blit(playerText, (0, gs.yFactor*(gs.rows+1)))
            self.win.blit(lvlText, (0, gs.yFactor*(gs.rows+1.5)))
            self.win.blit(
                scrText,
                (gs.xFactor*(gs.cols//2), gs.yFactor*(gs.rows+1))
            )

            # If player 2 reaches his finish
            if p2.y > gs.rows*gs.yFactor:
                p2Playing = False
                status = 1
                p2.score += gs.completeScore

            pygame.display.update()

        time.sleep(0.5)
        # If not last level of the game then only display switch player screen
        if(self.lvl != gs.noOfLvls):
            self.switchPlayersMsg(status, p2.score)

# Class for moving obstacles

# Import pygame libraries
import pygame

# Import config file
from config import GlobalSettings
gs = GlobalSettings()


class MovingObstacle():
    def __init__(self, win, row, col, direc, obsVel):
        self.row = row
        self.col = col
        self.direc = direc
        self.x = col * gs.xFactor
        self.y = row * gs.yFactor
        self.width = 1 * gs.xFactor
        self.height = 1 * gs.yFactor
        self.win = win
        self.color = (255, 255, 0)
        self.obsVel = obsVel
        self.image = pygame.image.load(gs.knifeRightImage)

        # Scale image to grid size
        self.image = pygame.transform.scale(
            self.image,
            (gs.xFactor, gs.yFactor)
        )

        # If objectis moving left then flip the image on the vert axis
        if(self.direc == 0):
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self):
        if self.direc == 1:
            self.x += self.obsVel
        else:
            self.x -= self.obsVel

    # Draw function to display image on screen
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))

    # Check if image is on border
    # If image is on border then it will appear from left
    # as it dissappears from right and vice versa
    def checkOnEdge(self):
        if self.direc == 1:
            if self.x > gs.screenWidth:
                self.x = -gs.xFactor
        elif self.direc == 0:
            if self.x < -gs.xFactor:
                self.x = gs.screenWidth

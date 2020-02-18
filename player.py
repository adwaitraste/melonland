# Class for player

# Import pygame libraries
import pygame

# Import config file
from config import GlobalSettings
gs = GlobalSettings()


class Player():
    def __init__(self, win, x, y, no):
        self.no = no

        # Load different images for player 1 and 2 respectively
        if(self.no == 1):
            self.image = pygame.image.load(gs.p1Image)
        else:
            self.image = pygame.image.load(gs.p2Image)

        # Scale image to grid size
        # Scale image to 70 % of x factor
        # Scale image to 95 % of y factor
        self.image = pygame.transform.scale(
            self.image,
            ((int)(0.70 * gs.xFactor), (int)(0.95 * gs.yFactor))
        )
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.x = x + (gs.xFactor/2) - (self.width/2)    # Scale hitbox to img
        self.y = y + (gs.yFactor/2) - (self.height/2)   # Scale hitbox to img
        self.xVel = 1 * gs.xFactor
        self.yVel = 1 * gs.yFactor
        self.win = win
        self.isInvincible = False
        self.score = 0
        self.gridX = 0
        self.gridY = 0

    def move(self, direction):
        if direction == "up":
            self.y -= self.yVel
            self.gridY -= self.yVel
            if(self.no == 1):
                if((self.gridY // gs.yFactor) % 2 == 0):    # Scoring
                    self.score += gs.mobsScore
                else:
                    self.score += gs.fobsScore
            else:
                if((self.gridY // gs.yFactor) % 2 == 0):    # Scoring
                    self.score -= gs.fobsScore
                else:
                    self.score -= gs.mobsScore

        if direction == "down":
            self.y += self.yVel
            self.gridY += self.yVel
            if(self.no == 2):
                if((self.gridY // gs.yFactor) % 2 == 0):    # Scoring
                    self.score += gs.mobsScore
                else:
                    self.score += gs.fobsScore
            else:
                if((self.gridY // gs.yFactor) % 2 == 0):    # Scoring
                    self.score -= gs.fobsScore
                else:
                    self.score -= gs.mobsScore

        if direction == "left":
            self.x -= self.xVel
        if direction == "right":
            self.x += self.xVel

    # Draw function to display image on screen
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))

    # Check if player has collided with the obstacle given as argument
    def isCollided(self, obj):
        if not self.isInvincible:
            if (self.x > obj.x + obj.width or obj.x > self.x + self.width):
                return False
            if (self.y > obj.y + obj.height or obj.y > self.y + self.height):
                return False
            return True
        return False

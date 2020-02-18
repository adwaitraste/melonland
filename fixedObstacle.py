# Class for fixed obstacles

# Import pygame libraries
import pygame

# Import config file
from config import GlobalSettings
gs = GlobalSettings()


class FixedObstacle():
    def __init__(self, win, row, col):
        self.row = row
        self.col = col
        self.x = col * gs.xFactor
        self.y = row * gs.yFactor
        self.width = 1 * gs.xFactor
        self.height = 1 * gs.yFactor
        self.win = win
        self.color = (0, 0, 0)
        self.image = pygame.image.load(gs.voidImage)

        # Scale image to grid size
        self.image = pygame.transform.scale(
            self.image,
            (gs.xFactor, gs.yFactor)
        )

    # Draw function to display image on screen
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))

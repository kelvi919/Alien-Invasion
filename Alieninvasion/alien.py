import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien."""
    def __init__(self, ai_game):
        """initialize the alien  and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its attribute.
        self.image_image = pygame.image.load("Alieninvasion\\Alieninvasion\\images\\alien.png")
        self.image = pygame.transform.scale(self.image_image, (70,70))
        self.rect = self.image.get_rect()

        # start each new alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal postiton.
        self.x = float(self.rect.x) 
        
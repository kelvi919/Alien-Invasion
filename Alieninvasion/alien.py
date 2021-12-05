import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien."""
    def __init__(self, ai_game):
        """initialize the alien  and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its attribute.
        self.image_image = pygame.image.load("Alieninvasion\Alieninvasion\images\ship.png")
        self.image = pygame.transform.scale(self.image_image, (self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()

        # start each new alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal postiton.
        self.x = float(self.rect.x) 


    def update(self):
        """"move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """return true if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        
        if self.rect.right == screen_rect.right:
            return True
        if self.rect.left == screen_rect.left:
            self.settings.fleet_direction = 1

        
        
            
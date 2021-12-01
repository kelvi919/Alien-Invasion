import pygame

class Ship:
    """a class to  manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # load the ship image and get its rect.
        self.image_image = pygame.image.load("Alieninvasion\\Alieninvasion\\images\\ship.png") #n note:Use the relative path from the image file
        self.image_rotate = pygame.transform.rotate(self.image_image, (180))
        self.image = pygame.transform.scale(self.image_rotate, (50, 50))
        self.rect = self.image.get_rect()
        

        # start euch ship at the midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom


        # store a float value for the ships horizontal position
        self.x = float(self.rect.x)


        # movement flag
        self.moving_right = False
        self.moving_left = False
    


    def update(self):
        """update the ships position based on the movement flag"""
        # update the ship.x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect value from self.x
        self.rect.x = self.x



    def blitme(self):
        """draws the ship"""
        self.screen.blit(self.image, self.rect)

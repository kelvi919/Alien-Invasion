import pygame
import sys
from settings import Settings
from ship import Ship 

class AlienInvasion:
    """overall class to manage game assets and behavios"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()


        self.settings = Settings()
        

        # Window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Kelvis Invasion")    
        
        
        self.ship = Ship(self)#asdasd

        

    def run_game(self):
        """main loop for the game"""
        while True: 
            self._check_events()
            self.ship.update()
            self._update_screen()



    def _check_events(self):
        """respond to keypresses and mouse movement"""
        # checks for events in the game
        for event in pygame.event.get():

            # checks for quit
            if event.type == pygame.QUIT:
                sys.exit()
            

            # moves the ship to the right/left
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d: 
                    self.ship.moving_right = True
                if event.key == pygame.K_a:
                    self.ship.moving_left = True

            # stops movement right/leftadad
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                if event.key == pygame.K_a:
                    self.ship.moving_left = False
                    
                    


    def _update_screen(self):
        """update img on the screen and flip to nthe new screen"""
        # redraw the screen
        self.screen.fill(self.settings.bg_color)# set background color
        self.ship.blitme()
        

        # draw the most recent screen
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
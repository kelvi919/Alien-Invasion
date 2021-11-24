import pygame
import sys

from settings import Settings
from ship import Ship 
from bullet import Bullet

class AlienInvasion:
    """overall class to manage game assets and behavios"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()


        self.settings = Settings()
        

        # Window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Kelvis Invasion")    
        
        
        self.ship = Ship(self)

        
    def run_game(self):
        """main loop for the game"""
        while True: 
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        """respond to keypresses and mouse movement"""
        # checks for events in the game
        for event in pygame.event.get():
            # checks for quit
            if event.type == pygame.QUIT:
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
                    

    def _update_screen(self):
        """update img on the screen and flip to nthe new screen"""
        # redraw the screen
        self.screen.fill(self.settings.bg_color)# set background color
        self.ship.blitme()
        

        # draw the most recent screen
        pygame.display.flip()


    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_d: 
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """respond to keyt releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        

    
    def _fire_bullet(self):
        """create a new bullet and add it to the bullet_list group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

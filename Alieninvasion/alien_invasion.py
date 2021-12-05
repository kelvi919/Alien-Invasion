import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """overall class to manage game assets and behaviors"""
    ### MAIN ###
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        # Window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Kelvis Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._check_fleet_edges()
            self._update_aliens()
            self._update_screen()


    def _update_screen(self):
        """update img on the screen and flip to the new screen"""
        # redraw the screen
        self.screen.fill(self.settings.bg_color)  # set background color
        self.ship.blitme()

        # drawing the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)



        # draw the most recent screen
        pygame.display.flip()
    ### MAIN ###


    ### EVENTS ###
    def _check_events(self):
        """respond to keypress and mouse movement"""
        # checks for events in the game
        for event in pygame.event.get():
            # checks for quit
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
    ### EVENTS ###


    ### BULLET ###
    def _fire_bullet(self):
        """create a new bullet and add it to the bullet_list group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            print("piuu")
    
    
    def _update_bullets(self):
        """update the bullets and get rid of the old bullets."""
        self.bullets.update()
        # getting rid of the bullets after the bullet.y is < 0
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # check for bullets that hits alien, if so delete alien and bullet
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True ,True)

    ### BULLET ###


    ### ALIEN ###
    def _create_alien(self, alien_num, row_num):
        """create an alien and set it into the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
        self.aliens.add(alien)


    def _create_fleet(self):
        """create the fleet of aliens"""
        # create an alien to find the number aliens in a row.
        # spacing between each aliens is ewual to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        availebele_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = availebele_space_y // (2 * alien_height)

        # create the full fleet of aliens.
        for row_num in range(number_rows):
            for alien_num in range(number_aliens_x):
                self._create_alien(alien_num, row_num)
        print(alien_num)


    def _update_aliens(self):
        """check if the fleet is at an edge, update the aliens position"""
        self._check_fleet_edges()
        self.aliens.update()
    

    def _check_fleet_edges(self):
        """respond appropriarely if ant aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():   
                self._change_fleet_direction()
                break
        
              
    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        if alien.check_edges():
            self.settings.fleet_direction = -1
    ### ALIEN ###

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

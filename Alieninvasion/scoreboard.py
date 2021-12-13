import pygame.font


class Scoreboard:
    """a class to show the socre information"""

    def __init__(self, ai_game):
        """initalize scorekeeping information"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scroing information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 60)

        # prepate the intial score image.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """turn the score into a rendert image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):    
        """turn the high score into a renderd image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color) 

        # center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 



    def check_high_score(self):
        """check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """turn the level into a renderd image"""
        level_str = str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
   
        # position the level below the score.
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """drawing on the screen"""
        self.screen.blit(self.score_image, self.score_rect) 
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
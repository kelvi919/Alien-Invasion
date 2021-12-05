class Settings:
    """a class that stores alle the settings for alien invasion"""

    def __init__(self):
        """iniitialize the games settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 70)
              
        # ship setting
        self.ship_speed = 1.0

        # bullet settings
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        # alien settings
        self.alien_speed = 0.5
        self.alien_width = 60
        self.alien_height = 60
        self.fleet_drop_speed = 10   
        self.fleet_direction = -1 # 1 == -right-> and 1- == <-left-
class Settings:
    """a class that stores alle the settings for alien invasion"""

    def __init__(self):
        """iniitialize the games settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 40, 40)
              
        # ship setting
        self.ship_speed = 0.5

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
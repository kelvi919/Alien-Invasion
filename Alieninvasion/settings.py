class Settings:
    """a class that stores alle the settings for alien invasion"""

    def __init__(self):
        """iniitialize the games static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 70)
              
        # ship setting
        self.ship_speed = 1.0

        # bullet settings
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        # alien settings
        self.ship_limit = 3
        self.alien_width = 60
        self.alien_height = 60
        self.fleet_drop_speed = 10  
        
        # how fast the game speeds up.
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        # scoring
        self.alien_points = 50

        # increasing point value
        self.score_scale = 1.5
        

    def initialize_dynamic_settings(self):
        """initialivze settings that change throuout the game"""
        self.ship_speed = 0.3
        self.bullet_speed = 1.0
        self.alien_speed = 0.1
        
        self.fleet_direction = 1 # 1 == right -> / 1- == <- left

    
    def increase_speed(self):
        """increase speed settings and point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)




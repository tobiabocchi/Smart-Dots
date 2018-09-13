from Globals import *


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(goal_size)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = goal_coord

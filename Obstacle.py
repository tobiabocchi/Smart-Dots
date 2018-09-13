from Globals import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, topleft):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(obs_size)
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.add(all_sprites)
        self.add(obs_sprites)

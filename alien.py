import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game_settings,screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("images/ment.png")
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

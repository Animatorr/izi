import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game_setinngs,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,game_setinngs.bullet_width,game_setinngs.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.color = game_setinngs.bullet_color
        self.speed = game_setinngs.bullet_speed_factor
    def update(self):
        self.rect.y-=self.speed
    def drawbullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

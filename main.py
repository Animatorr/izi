import pygame , sys
import gamefunction as gf
from setinngs import Setinngs
from ship import Ship
from pygame.sprite import Group
from bg import Bg
from alien import Alien
def init_game():
    pygame.init()
    game_setinngs=Setinngs()
    screen=pygame.display.set_mode((game_setinngs.screen_width,game_setinngs.screen_height))
    ship = Ship(screen)
    bullets = Group()
    bg = Bg(screen)
    alien = Group()
    gf.create_fleet(game_setinngs, screen, alien)
    pygame.display.set_caption("gamenambawan")
    create_fleet(game_setinngs, screen, alien)
    while True:
        gf.checkevents(game_setinngs,screen,ship, bullets)
        gf.update_screen(bg,ship,bullets,alien)
        ship.update()

        gf.update_bullets(bullets)
        gf.updatescreen(bg,ship,bullets)

init_game()
import pygame , sys
from bullet import Bullet
from alien import Alien

def checkevents(game_setinngs,screen,ship, bullets):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            check_keydown_events(game_setinngs,screen,ship, e, bullets)
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                ship.moving_right=False
            if e.key == pygame.K_LEFT:
                ship.moving_left=False
            if e.key == pygame.K_UP:
                ship.moving_up=False
            if e.key == pygame.K_DOWN:
                ship.moving_down=False

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def updatescreen(bg,ship,bullets,alien):
    bg.update()
    ship.bleedme()
    alien.bleedme()
    alien.draw(screen)
    for bullet in bullets.sprites():
        bullet.drawbullet()
    pygame.display.flip()

def check_keydown_events(game_setinngs,screen,ship, e, bullets):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = True
    if e.key == pygame.K_LEFT:
        ship.moving_left = True
    if e.key == pygame.K_UP:
        ship.moving_up = True
    if e.key == pygame.K_DOWN:
        ship.moving_down = True
    if e.key == pygame.K_SPACE:
        if len(bullets) < game_setinngs.bullets_allowed:
            new_bullet = Bullet(game_setinngs, screen, ship)
            bullets.add(new_bullet)
def create_fleet(game_setinngs, screen, aliens):
    alien = Alien(game_setinngs, screen)
    alien_width=alien.rect.width
    availible_space_x = game_setinngs.screen.width - 2 * alien_width
    number_aliens_x=int(availible_space_x /(2 *alien_width))
    for alien_number in range(number_aliens_x):
        alien=Alien(game_setinngs,screen)
        alien.x=alien_width +2 *alien_width *alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

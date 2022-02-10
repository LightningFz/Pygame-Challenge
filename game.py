from turtle import Screen, update
from player import PlayerSprite
from enemy import EnemySprite
from random import randrange
import pygame, sys
pygame.init()

#Varables
Green = ( 53, 96, 59)
Light_brown = ( 163, 143, 72)
Moving_speed = 8
clock = pygame.time.Clock()

#Game Screen 
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("48 hours game")

background = pygame.image.load("background.png")


player = PlayerSprite(400, 300) #creating the player sprit
player_rect = player.rect
enemyOne = EnemySprite()
enemyOne_rect = enemyOne.rect
enemyTwo = EnemySprite()
enemyTwo_rect = enemyTwo.rect
enemyThree = EnemySprite()
enemyThree_rect = enemyThree.rect
enemyFour = EnemySprite()
enemyFour_rect = enemyFour.rect
enemyFive = EnemySprite()
enemyFive_rect = enemyFive.rect
enemySix = EnemySprite()
enemySix_rect = enemySix.rect
enemySeven = EnemySprite()
enemySeven_rect = enemySeven.rect
enemyEight = EnemySprite()
enemyEight_rect = enemyEight.rect
enemyNine = EnemySprite()
enemyNine_rect = enemyNine.rect
enemyTen = EnemySprite()
enemyTen_rect = enemyTen.rect
enemyEleven = EnemySprite()
enemyEleven_rect = enemyEleven.rect
enemyTwelve = EnemySprite()
enemyTwelve_rect = enemyTwelve.rect
enemyFou = EnemySprite()
enemyFou_rect = enemyFou.rect
enemyFiv = EnemySprite()
enemyFiv_rect = enemyFiv.rect
enemySi = EnemySprite()
enemySi_rect = enemySi.rect
enemySeve = EnemySprite()
enemySeve_rect = enemySeve.rect
enemyEigh = EnemySprite()
enemyEigh_rect = enemyEigh.rect
enemyNin = EnemySprite()
enemyNin_rect = enemyNin.rect
open = True
def boom():
    if player_rect.colliderect(enemyOne_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyTwo_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyThree_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyFour_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyFive_rect):
        pygame.quit()
    elif player_rect.colliderect(enemySix_rect):
        pygame.quit()
    elif player_rect.colliderect(enemySeven_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyEight_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyNine_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyTen_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyTw_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyThre_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyFou_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyFiv_rect):
        pygame.quit()
    elif player_rect.colliderect(enemySi_rect):
        pygame.quit()
    elif player_rect.colliderect(enemySeve_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyEigh_rect):
        pygame.quit()
    elif player_rect.colliderect(enemyNin_rect):
        pygame.quit()
#-------------------MAIN LOOP--------------------
while open==True:#loop for the window to stay open
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            open=False
        
        #by pressing x the game will quit
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: 
                open=False

        
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(Moving_speed)
    if keys[pygame.K_RIGHT]:
        player.moveRight(Moving_speed)
    if keys[pygame.K_UP]:
        player.moveUp(Moving_speed)
    if keys[pygame.K_DOWN]:
        player.moveDown(Moving_speed)
    
    
    #--game logic--
    boom()
    player.Update()
    enemyOne.Update()
    enemyTwo.Update()
    enemyThree.Update()
    enemyFour.Update()
    enemyFive.Update()
    enemySix.Update()
    enemySeven.Update()
    enemyEight.Update()
    enemyNine.Update()
    enemyTen.Update()
    enemyTw.Update()
    enemyThre.Update()
    enemyFou.Update()
    enemyFiv.Update()
    enemySi.Update()
    enemySeve.Update()
    enemyEigh.Update()
    enemyNin.Update()  

    #--drawing code--

    all_sprites_list = pygame.sprite.Group()  #creating a group for all sprites
    all_sprites_list.add(player) #adding the sprite to group
    all_sprites_list.add(enemyOne)
    all_sprites_list.add(enemyTwo)
    all_sprites_list.add(enemyThree)
    all_sprites_list.add(enemyFour)
    all_sprites_list.add(enemyFive)
    all_sprites_list.add(enemySix)
    all_sprites_list.add(enemySeven)
    all_sprites_list.add(enemyEight)
    all_sprites_list.add(enemyNine)
    all_sprites_list.add(enemyTen)
    all_sprites_list.add(enemyTw)
    all_sprites_list.add(enemyThre)
    all_sprites_list.add(enemyFou)
    all_sprites_list.add(enemyFiv)
    all_sprites_list.add(enemySi)
    all_sprites_list.add(enemySeve)
    all_sprites_list.add(enemyEigh)
    all_sprites_list.add(enemyNin)

    
    all_sprites_list.update()
    #update the screen
    screen.blit(background,(0,0))
    all_sprites_list.draw(screen)
    pygame.display.flip()

    #Limit fps to 60
    clock.tick(60)

#end the game
pygame.quit()
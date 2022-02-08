from email.mime import image
import pygame
from random import randrange


enemy_postion_x = randrange(20, 780)
enemy_postion_y = randrange(20, 580)
pixX = randrange(-20, 20)
pixY = randrange(-20, 20)

class EnemySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.timer = randrange(60, 120)
        self.enemy_dir_x = randrange(0, 260)
        self.enemy_dir_y = randrange(0, 260) 
        self.rect.center = [enemy_postion_x,enemy_postion_y]

    
    def Update(self):
        if self.rect.x <= 0:
            print("at the border-left")
            self.rect.x = 0
            self.enemy_dir_x = randrange(-800, 800)
        elif self.rect.x >= 770:
            print("at the border-rt")
            self.rect.x = 770
            self.enemy_dir_x = randrange(-800, 800)
        elif self.rect.y <= 0:
            print("at the border-top")
            self.rect.y = 0
            self.enemy_dir_y = randrange(-600, 600)
        elif self.rect.y >= 570:
            print("at the border-btm")
            self.rect.y = 570
            self.enemy_dir_y = randrange(-600, 600)
        if self.timer > 0:   
        
            #======random movement at the X axis=======
            moveSpeed = randrange(3, 10)
            if self.enemy_dir_x < 0:
                if self.rect.x >= self.enemy_dir_x:#========LEFT=====
                    self.rect.x -= moveSpeed
            elif self.enemy_dir_x > 0:
                if self.rect.x <= self.enemy_dir_x:#========RIGHT====
                    self.rect.x += moveSpeed


            #======random movement at the Y axis=======
            if self.enemy_dir_y < 0:
                if self.rect.y >= self.enemy_dir_y:#=========UP======
                    self.rect.y -= moveSpeed
            if self.enemy_dir_y > 0:
                if self.rect.y <= self.enemy_dir_y:#========DOWN=====
                    self.rect.y += moveSpeed
            
            #else:
                #self.rect.x = self.enemy_dir_x
                #self.rect.y = self.enemy_dir_y
            self.timer -= 1
        else:
            self.enemy_dir_x = randrange(-800, 800)
            self.enemy_dir_y = randrange(-600, 600)
            self.timer = randrange(30, 180)

        


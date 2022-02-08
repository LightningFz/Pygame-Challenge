from hashlib import new
from turtle import width
import pygame, sys


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def Update(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 770:
            self.rect.x = 770
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 570:
            self.rect.y = 570 

    def moveRight(self, pixels):
        new = self.rect.x + pixels
        self.rect.x = new

    def moveLeft(self, pixels):
        new = self.rect.x - pixels
        self.rect.x = new

    def moveUp(self, pixels):
        new = self.rect.y - pixels
        self.rect.y = new

    def moveDown(self, pixels):
        new = self.rect.y + pixels
        self.rect.y = new



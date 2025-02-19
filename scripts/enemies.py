import pygame, random


enemies_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load("data/carp.png")
        self.image = pygame.transform.scale(self.image, (100, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 1240
        self.complete = False
        self.rect.y = y
        self.vx = 0
        enemies_group.add(self)

    def update(self):
        self.vx = -3
        self.rect.x += self.vx
        if self.rect.x <= 0:
            enemies_group.remove(self)
            print(self, 'deleted')
            del self

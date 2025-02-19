import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.SOURCE_IMG + "car.png")
        self.image = pygame.transform.scale(self.image, (100, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.vy = 0

    def update(self):
        if self.rect.y >= 630:
            self.rect.y = 620
        elif self.rect.y <= 0:
            self.rect.y = 10
        else:
            self.rect.y += self.vy
        self.vy = 0

    def to_up(self):
        self.vy = -1

    def to_down(self):
        self.vy = 1

    def check_coll(self, group: pygame.sprite.Group):
        hits = pygame.sprite.spritecollide(self, group, True)
        return hits

    def update_count(self, group: pygame.sprite.Group):
        s = 0
        for e in group:
            print(e, e.rect.x)
            if e.rect.x <= self.rect.x and not e.complete:
                e.complete = True
                s += 1
        return s
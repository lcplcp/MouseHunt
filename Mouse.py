import pygame
import sys
import random


class Mouse(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.status = [pygame.image.load("a1.png"),
                       pygame.image.load("a2.png"),
                       pygame.image.load("a3.png")]
        for i in range(len(self.status)):
            self.status[i] = pygame.transform.scale(self.status[i], (60, 60))
        self.rect = self.status[0].get_rect()
        self.rect = self.rect.inflate(-50, -50)
        self.rect = self.rect.move(x, y)
        self.freq = 10
        self.freq_count = 0
        self.status_index = 0
        self.image = self.status[self.status_index]
        self.dead = False
        self.rect.move_ip(-20, -20)
        self.live = False
        self.blood = 60

    def update(self) -> None:
        self.updata_image()
        self.updateLifeSpan()

    def updata_image(self):
        if self.freq_count >= self.freq:
            self.status_index += 1
            if self.status_index > 2:
                self.status_index = 0
            self.image = self.status[self.status_index]
            self.freq_count = 0
        else:
            self.freq_count += 1

    def updateLifeSpan(self) -> None:
        if self.live:
            if self.blood >0:
                self.blood -= 1
            else:
                self.live = False
                self.blood = 60

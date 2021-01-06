import pygame


class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("c.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-60, -60)

    def update(self) -> None:
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
        self.rect.move_ip(-30, -30)

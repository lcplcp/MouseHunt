import pygame


class Boom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("b.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        # self.rect = self.rect.inflate(-60, -60)


    def update(self) -> None:
        print('------')
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def Change(self) -> None:
        iBoomFreshTime = 0
        while iBoomFreshTime < 60:
            iBoomFreshTime += 1


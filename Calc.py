import pygame
import sys
import random
import Boom

iNumLimit = 4
iNumList = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def calcs(AllMouses, mouse_list, AllHammer, AllBoom, screen, background):
    score = 0  #计分项
    clock = pygame.time.Clock()  # 设置时钟
    iMousFreshTime = 0
    while True:
        if iMousFreshTime >= 30:
            iMousFreshTime = 0
            if len(AllMouses.sprites()) == 0:
                RangMouse_list = random.sample(iNumList, iNumLimit)
                for iNum in RangMouse_list:
                    AllMouses.add(mouse_list[iNum])
            elif len(AllMouses.sprites()) < iNumLimit:
                for eachMouses in AllMouses:
                    AllMouses.remove(eachMouses)
        else:
            iMousFreshTime += 1
        clock.tick(60)  # 每秒执行60次

        Hit = False
        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                collisions = pygame.sprite.groupcollide(AllMouses, AllHammer, True, False)
                if collisions:
                    score += 1
                    print('Score is: ', score)
                    Hit = True

                    # for eachBoom in AllBoom:
                    #     AllBoom.remove(eachBoom)
                    #
                    # AllBoom.add()

                else:
                    Hit = False

                    # boom. self.image = pygame.image.load("b.png")




        if Hit:
            AllBoom.update()
        AllMouses.update()
        AllHammer.update()
        screen.fill((255, 255, 255))  # 填充颜色
        screen.blit(background, (0, 0))  # 填入到背景
        AllMouses.draw(screen)
        AllHammer.draw(screen)
        if Hit:
            AllBoom.draw(screen)

        pygame.display.flip()
import pygame
import sys
import random
import Mouse
import Hammer
import Boom
from Calc import calcs

origin_Pos = (0, 0)
mouse1_PosX, mouse1_PosY = 85, 75
mouse2_PosX, mouse2_PosY = 205, 75
mouse3_PosX, mouse3_PosY = 325, 75
mouse4_PosX, mouse4_PosY = 70, 140
mouse5_PosX, mouse5_PosY = 205, 140
mouse6_PosX, mouse6_PosY = 325, 140
mouse7_PosX, mouse7_PosY = 65, 210
mouse8_PosX, mouse8_PosY = 205, 210
mouse9_PosX, mouse9_PosY = 340, 210

def initProcessAndFont():
    pygame.init()  # 初始化pygame
    pygame.font.init()  # 初始化字体
    font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小

def initScreen():
    size = width, height = 494, 338  # 设置窗口
    screen = pygame.display.set_mode(size)  # 显示窗口
    return screen

def initBackground():
    background = pygame.image.load("d.png")  # 加载背景图片
    return background

def initMouseList():
    mouse1 = Mouse.Mouse(mouse1_PosX, mouse1_PosY)
    mouse2 = Mouse.Mouse(mouse2_PosX, mouse2_PosY)
    mouse3 = Mouse.Mouse(mouse3_PosX, mouse3_PosY)
    mouse4 = Mouse.Mouse(mouse4_PosX, mouse4_PosY)
    mouse5 = Mouse.Mouse(mouse5_PosX, mouse5_PosY)
    mouse6 = Mouse.Mouse(mouse6_PosX, mouse6_PosY)
    mouse7 = Mouse.Mouse(mouse7_PosX, mouse7_PosY)
    mouse8 = Mouse.Mouse(mouse8_PosX, mouse8_PosY)
    mouse9 = Mouse.Mouse(mouse9_PosX, mouse9_PosY)
    mouse_list = [mouse1, mouse2, mouse3,
                  mouse4, mouse5, mouse6,
                  mouse7, mouse8, mouse9]
    return mouse_list

if __name__ == '__main__':
    """主程序"""
    initProcessAndFont()

    screen = initScreen()  # 显示窗口

    background = initBackground()

    screen.blit(background, origin_Pos)

    mouse_list = initMouseList() #初始化老鼠数组
    hammer = Hammer.Hammer()     #初始化锤子数组
    boom = Boom.Boom()     #初始化Boom数组

    AllMouses = pygame.sprite.RenderPlain(())     #初始化老鼠精灵组
    AllHammer = pygame.sprite.RenderPlain(hammer) #初始化锤子精灵组
    AllBoom = pygame.sprite.RenderPlain(()) #初始化Boom精灵组

    calcs(AllMouses, mouse_list, AllHammer, AllBoom, screen, background)

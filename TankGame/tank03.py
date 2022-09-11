"""
v1.03
    新增功能：
        创建游戏窗口
        用到游戏引擎中的功能模块
        官方开发文档
"""

import pygame
Color_Black = pygame.Color(0, 200, 0)
class MainGame():
    #游戏主窗口
    window = None
    Screen_Height = 550
    Screen_Width = 900
    #开始游戏方法
    def startGame(self):
        pygame.display.init()
        #创建窗口，加载窗口（借鉴官方文档）set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
        MainGame.window = pygame.display.set_mode([MainGame.Screen_Width, MainGame.Screen_Height])
        #设置游戏标题
        pygame.display.set_caption("坦克大战v1.03")
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色 Surface.fill(color)
            MainGame.window.fill(Color_Black)
            #刷新屏幕
            pygame.display.update()

    #结束游戏方法
    def endGame(self):
        print('谢谢使用')
        #结束python解释器
        exit()
class Tank():
    def __init__(self):
        pass
    #坦克移动的方法
    def move(self):
        pass
    #坦克射击的方法
    def shoot(self):
        pass
    #坦克展示的方法
    def displayTank(self):
        pass
class MyTank(Tank):
    def __init__(self):
        pass
class EnemyTank(Tank):
    def __init__(self):
        pass
class Bullet():
    def __init__(self):
        pass
    #子弹移动的方法
    def move(self):
        pass
    #子弹展示的方法
    def displayBullet(self):
        pass
class explode:
    def __init__(self):
        pass
    #展示爆炸效果
    def displayExplode(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass

MainGame().startGame()


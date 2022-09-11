"""
v1.04
    新增功能：
        事件处理：1、点击关闭按钮，能够退出程序；2、方向控制，子弹发射

"""

import pygame
Color_Black = pygame.Color(0, 200, 0)
Version = 'v1.04'
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
        pygame.display.set_caption("坦克大战"+Version)
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色 Surface.fill(color)
            MainGame.window.fill(Color_Black)
            #在循环中持续完成事件的获取
            self.getEvent()
            #刷新屏幕
            pygame.display.update()

    #获取程序运行期间的所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        # 1、获取所有事件
        eventList = pygame.event.get()
        # 2、对事件进行判断处理（1、点击关闭按钮  2、按下键盘上的某个按键）
        for event in eventList:
            #判断event.type是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            #判断event.type是否为按键按下，如果是的话继续判断按键是哪一个按键，然后再进行对应事件处理
            if event.type == pygame.KEYDOWN:
                #具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:
                    print('坦克向左掉头，移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右掉头，移动')
                elif event.key == pygame.K_UP:
                    print('坦克向上掉头，移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克向下掉头，移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')

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


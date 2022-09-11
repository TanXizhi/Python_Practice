"""
2、明白需求（基于面向对象的分析）：
    1、有哪些类：  2、不同的类所具备的一些功能：
        1、主逻辑类
            开始游戏
            结束游戏
        2、坦克类（1、我方坦克  2、敌方坦克）：坦克父类然后子类继承父类
            移动
            射击
            展示坦克
        3、子弹类
            移动
            展示子弹
        4、爆炸效果类
            展示爆炸效果
        5、墙壁类
            没有功能，但是有属性。属性：是否可以通过
        6、音效类
            播放音乐

3、坦克大战项目框架的搭建
    涉及到的类，用代码简单地实现

"""

import pygame
class MainGame():
    def __init__(self):
        pass
    #开始游戏方法
    def startGame(self):
        pass
    #结束游戏方法
    def endGame(self):
        pass
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




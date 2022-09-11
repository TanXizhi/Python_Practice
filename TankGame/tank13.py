"""
v1.13
    1、完善子弹的发射功能
        tank 发射子弹  -> 产生一颗子弹

"""

import pygame,time,random
Color_Black = pygame.Color(0, 0, 0)
Color_Red = pygame.Color(255, 0, 0)
Version = 'v1.13'
class MainGame():
    #游戏主窗口
    window = None
    Screen_Height = 500
    Screen_Width = 900
    #创建我方坦克
    TANK_P1 = None
    #存储所有敌方坦克
    EnemyTank_list = []
    #要创建的敌方坦克数量
    EnemyTank_count = 5
    #存储我方子弹的列表
    Bullet_list = []
    #开始游戏方法
    def startGame(self):
        pygame.display.init()
        #创建窗口，加载窗口（借鉴官方文档）set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
        MainGame.window = pygame.display.set_mode([MainGame.Screen_Width, MainGame.Screen_Height])
        #创建我方坦克
        MainGame.TANK_P1 = Tank(400,300)
        #创建敌方坦克
        self.creatEnemyTank()
        #设置游戏标题
        pygame.display.set_caption("坦克大战"+Version)
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色 Surface.fill(color)
            MainGame.window.fill(Color_Black)
            #在循环中持续完成事件的获取
            self.getEvent()
            #将绘制文字得到的小画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface('剩余敌方坦克%d辆'%len(MainGame.EnemyTank_list)),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #循环展示敌方坦克
            self.blitEnemyTank()
            #根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            #调用渲染子弹列表的方法
            self.blitBullet()
            time.sleep(0.02)
            #刷新屏幕
            pygame.display.update()
    #创建敌方坦克
    def creatEnemyTank(self):
        top = 100
        speed = random.randint(3,6)
        for i in range(MainGame.EnemyTank_count):
            #每次都随机生成一个left值
            left = random.randint(1, 8)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_list.append(eTank)

    #将敌方坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            #坦克的移动方法
            eTank.randMove()

    #将子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            bullet.displayBullet()

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
                    #修改坦克的方向
                    MainGame.TANK_P1.direction = 'L'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右掉头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'R'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print('坦克向上掉头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'U'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print('坦克向下掉头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'D'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
                    # 产生一颗子弹
                    m = Bullet(MainGame.TANK_P1)
                    # 将子弹加入到子弹列表
                    MainGame.Bullet_list.append(m)
            if event.type == pygame.KEYUP:
                #松开的如果是方向键，才更改坦克的移动状态
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #修改坦克的移动状态
                    MainGame.TANK_P1.stop = True
    #左上角文字绘制的功能
    def getTextSurface(self, text):
        #初始化字体模块
        pygame.font.init()
        #查看系统支持的所有字体
        #fontList = pygame.font.get_fonts()
        #print(fontList)
        #选中一个合适的字体
        font = pygame.font.SysFont('songti',18)
        #使用对应的字符完成相关内容的绘制
        textSurface = font.render(text,True,Color_Red)
        return textSurface
    #结束游戏方法
    def endGame(self):
        print('谢谢使用')
        #结束python解释器
        exit()
class Tank():
    def __init__(self, left, top):
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'),
            'D':pygame.image.load('img/p1tankD.gif'),
            'L':pygame.image.load('img/p1tankL.gif'),
            'R':pygame.image.load('img/p1tankR.gif'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        #坦克所在区域 rect->
        self.rect= self.image.get_rect()
        #指定坦克初始化位置，分别距x,y轴的位置
        self.rect.left = left
        self.rect.top = top
        #新增速度属性
        self.speed = 5
        #新增属性：坦克的移动开关
        self.stop = True

    #坦克移动的方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.Screen_Width:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.Screen_Height:
                self.rect.top += self.speed

    #坦克射击的方法
    def shoot(self):
        return Bullet(self)
    #坦克展示的方法(将坦克这个surface绘制到窗口中 blit())
    def displayTank(self):
        #1、重新设置坦克的图片
        self.image = self.images[self.direction]
        #2、将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)

class MyTank(Tank):
    def __init__(self):
        pass
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在区域 rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置，分别距x,y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性：坦克的移动开关
        self.stop = True
        #新增步数属性，用来控制敌方坦克的随机移动
        self.step = 50

    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
    #随机移动
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1

class Bullet():
    def __init__(self,tank):
        #图片
        self.image = pygame.image.load('img/tankmissile.gif')
        #方向（同坦克方向）
        self.direction = tank.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 -self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        #速度
        self.speed = 7
    #子弹移动的方法
    def move(self):
        pass
    #子弹展示的方法
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
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


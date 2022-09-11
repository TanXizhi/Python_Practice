"""
v1.22
    新增功能：
        1、实现子弹不可以穿墙
"""

import pygame,time,random
Color_Black = pygame.Color(0, 0, 0)
Color_Red = pygame.Color(255, 0, 0)
Version = 'v1.22'
class MainGame():
    #游戏主窗口
    window = None
    Screen_Height = 500
    Screen_Width = 920
    #创建我方坦克
    TANK_P1 = None
    #存储所有敌方坦克
    EnemyTank_list = []
    #要创建的敌方坦克数量
    EnemyTank_count = 5
    #存储我方子弹的列表
    Bullet_list = []
    #存储敌方子弹的列表
    Enemy_Bullet_list = []
    #爆炸效果列表
    Explode_list = []
    #墙壁列表
    Wall_list = []
    #开始游戏方法
    def startGame(self):
        pygame.display.init()
        #创建窗口，加载窗口（借鉴官方文档）set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
        MainGame.window = pygame.display.set_mode([MainGame.Screen_Width, MainGame.Screen_Height])
        #创建我方坦克
        self.creatMyTank()
        #创建敌方坦克
        self.creatEnemyTank()
        #创建墙壁
        self.creatWalls()
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
            #调用展示墙壁的方法
            self.blitWalls()
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                #将我方坦克加入到窗口中
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            #循环展示敌方坦克
            self.blitEnemyTank()
            #根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            #调用渲染我方子弹列表的方法
            self.blitBullet()
            #调用渲染敌方子弹列表的方法
            self.blitEnemyBullet()
            #调用爆炸效果展示爆炸效果的方法
            self.displayExplodes()
            time.sleep(0.02)
            #刷新屏幕
            pygame.display.update()
    #创建我方坦克的方法
    def creatMyTank(self):
        MainGame.TANK_P1 = Tank(400, 300)
    #创建敌方坦克的方法
    def creatEnemyTank(self):
        top = 100
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(3, 6)
            #每次都随机生成一个left值
            left = random.randint(1, 8)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_list.append(eTank)
    #创建墙壁的方法
    def creatWalls(self):
        for i in range(7):
            wall = Wall(130*i,200)
            MainGame.Wall_list.append(wall)
    #将墙壁加入到窗口中
    def blitWalls(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)
    #将敌方坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                #坦克的移动方法
                eTank.randMove()
                #调用敌方坦克的射击
                eBullet = eTank.shoot()
                #如果子弹为None, 不加入到列表
                if eBullet:
                    #将子弹存储到敌方子弹列表中
                    MainGame.Enemy_Bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)
    #将我方子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            #如果子弹还活着，绘制出来；否则，直接从列表中移除该子弹
            if bullet.live:
                bullet.displayBullet()
                #让子弹移动
                bullet.bulletMove()
                #调用我方子弹与敌方坦克碰撞的方法
                bullet.hitEnemyTank()
                #调用判断我方子弹是否碰撞到墙壁的方法
                bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(bullet)
    #将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for eBullet in MainGame.Enemy_Bullet_list:
            #如果子弹还活着，绘制出来；否则，直接从列表中移除该子弹
            if eBullet.live:
                eBullet.displayBullet()
                #让子弹移动
                eBullet.bulletMove()
                #调用判断敌方子弹是否碰撞到墙壁的方法
                eBullet.hitWalls()
                #调用敌方子弹与我方坦克碰撞的方法
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank()
            else:
                MainGame.Enemy_Bullet_list.remove(eBullet)

    #新增方法：展示爆炸效果列表
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)

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
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    self.creatMyTank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
                        if len(MainGame.Bullet_list) < 3:
                            # 产生一颗子弹
                            m = Bullet(MainGame.TANK_P1)
                            # 将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                        else:
                            print('子弹数量不足')
                        print('当前屏幕中的子弹数量为：%d'%len(MainGame.Bullet_list))
            if event.type == pygame.KEYUP:
                #松开的如果是方向键，才更改坦克的移动状态
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Tank(BaseItem):
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
        #新增属性 live用来记录坦克是否活着
        self.live = True

    #坦克移动的方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < MainGame.Screen_Width:
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
        super().__init__(left,top)
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
    #约束敌方子弹数量，重写父类的shoot
    def shoot(self):
        num = random.randint(1,1000)
        if num <= 20:
            return Bullet(self)
class Bullet(BaseItem):
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
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height/2 - self.rect.height/2
        #速度
        self.speed = 7
        #用来记录子弹是否活着
        self.live = True
    #子弹移动的方法
    def bulletMove(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                #撞到墙壁，修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < MainGame.Screen_Width:
                self.rect.left += self.speed
            else:
                # 撞到墙壁，修改状态值
                self.live = False
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 撞到墙壁，修改状态值
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.Screen_Height:
                self.rect.top += self.speed
            else:
                # 撞到墙壁，修改状态值
                self.live = False
    #子弹展示的方法
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
    #新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                #产生一个爆炸效果
                explode = Explode(eTank)
                #将爆炸效果加入到爆炸效果列表中
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False
    #新增敌方子弹与我方坦克的碰撞方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            #产生爆炸效果
            explode = Explode(MainGame.TANK_P1)
            #将爆炸效果加入到列表中
            MainGame.Explode_list.append(explode)
            #修改子弹状态
            self.live = False
            #修改我方坦克状态
            MainGame.TANK_P1.live = False
    #新增子弹与墙壁的碰撞
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                #修改子弹的状态
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False

class Explode():
    def __init__(self,tank):
        self.rect = tank.rect
        self.step = 0
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif'),
        ]
        self.image = self.images[self.step]
        self.live = True
    #展示爆炸效果
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        #用来判断墙壁是否应该在窗口中展示
        self.live = True
        #用来记录墙壁的生命值
        self.hp = 3
    #展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)

class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass

MainGame().startGame()


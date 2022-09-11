"""
1、游戏引擎的安装：
    安装方式有两种：
        1、通过pip安装
            在终端中输入pip install pycharm == 版本号
        2、通过pycharm安装
            pycharm-->preferences-->project-->python interpreter--> 左上角'+'install
            -->搜索框输入pycharm-->下方 install package
    验证pygame是否安装成功
        import pygame

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
"""
import pygame

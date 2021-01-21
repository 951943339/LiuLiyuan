import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形

        self.image = pygame.image.load("images/ship04.png")
        self.rect = self.image.get_rect()  # 飞船的外接矩形rectangle
        self.screen_rect = screen.get_rect()  # 飞船屏幕的外接矩形

        # 将每艘新飞船放在屏幕底部中央
        # 飞船初始位置：横向剧中，纵向底部对齐
        # 飞船底部中心x横坐标 = 窗口中心横坐标
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 飞船举行底部横纵坐标
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:  #self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        # self.rect.centerx -= 1
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上剧中"""

        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - 40

        # self.rect.bottom = self.screen_rect.bottom


        # self.centerb = self.screen_rect.centery

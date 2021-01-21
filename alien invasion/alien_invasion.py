import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.mixer.init()
    # 混音器初始化
    #sound = pygame.mixer.Sound("music/boom01.mp3")
    # 后面需要调用音效，就使用sound_effect.play()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    pygame.mixer.music.load("music/music03.mp3")
    pygame.mixer.music.play(-1)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # # 创建一个外星人
    #
    # alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # print(len(bullets))
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # 监视键盘和鼠标事件
    # 循环检查所获取的所有事件

    # for event in pygame.event.get():
    # # 如果事件的类型（type）是“退出”
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    #     # 让最近绘制的屏幕可见
    # screen.fill(ai_settings.bg_color)
    # ship.blitme()
    # pygame.display.flip()


run_game()

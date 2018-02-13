import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# 创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	ship = Ship(ai_settings, screen)
	sb = Scoreboard(ai_settings, screen, stats)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens) 
	
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active: 
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets) 
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
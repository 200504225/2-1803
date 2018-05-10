import pygame
from PlanSprite import *

class PlaneGame(object):
	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1500)
		self.enemy_group = pygame.sprite.Group()
	def start_game(self):
		print("开始游戏...")
		while True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __create_sprites(self):

		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 英雄组
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
	def __event_handler(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
	def __check_collide(self):
		pass

	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		
		self.hero_group.update()
		self.hero_group.draw(self.screen)
	def __game_over():

		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()

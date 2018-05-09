import pygame
from PlanSprite import *

class PlaneGame(object):
	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
	def start_game(self):
		print("开始游戏...")
		while True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __create_sprites(self):
		pass
	def __event_handler(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
		pass
	def __check_collide(self):
		pass

	def __update_sprites(self):
		pass
	def __game_over():
		"""游戏结束"""

		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()

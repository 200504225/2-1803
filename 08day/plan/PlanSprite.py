import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
		
	def update(self,*args):
		self.rect.y += self.speed

class Background(GameSprite):
#"""游戏背景精灵"""
	def __init__(self, is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):
#"""敌机精灵"""

	def __init__(self):
		image_name ="./images/enemy1.png"
		super().__init__("./images/enemy1.png",)
		self.speed = random.randint(1, 3)

		self.rect.bottom = 0

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)

	def __del__(self):
		print("敌机挂了 %s" % self.rect)

# 3. 设置敌机的随机初始位置

	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()

class Hero(GameSprite):
#"""英雄精灵"""

	def __init__(self):

		super().__init__("./images/me1.png", 0)
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

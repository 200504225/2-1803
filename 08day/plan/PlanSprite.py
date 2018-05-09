import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		super().__init__()
# 加载图像
		self.image = pygame.image.load(image_name)
# 设置尺寸
		self.rect = self.image.get_rect()
# 记录速度
		self.speed = speed
	def update(self):
# 默认在垂直方向移动
		self.rect.y += self.speed

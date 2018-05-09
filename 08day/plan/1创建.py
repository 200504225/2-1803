import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏...")

			pygame.quit()

# 直接退出系统
			exit()




pygame.quit()

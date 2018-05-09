import pygame,random
i = random.randint(1,5)
o = random.randint(1,5)
from PlanSprite import * 
pygame.init()
#背景
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
#pygame.display.update()
#飞机
hero = pygame.image.load("./images/hero.gif")
screen.blit(hero, (180,500))

clock = pygame.time.Clock()
hero_rect = pygame.Rect(180, 500, 200, 200)

#import random
#random.rand
enemy = GameSprite("./images/enemy1.png",o)
enemy1 = GameSprite("./images/enemy1.png",i)
enemy1.rect.x = 100
enemy_group = pygame.sprite.Group(enemy,enemy1)
#pygame.display.update()
i = 0
while True:

	clock.tick(100)
	hero_rect.x -= 10
	if hero_rect.x <= 0:
		hero_rect.x = 700
	hero_rect.y -= 4
	if hero_rect.y+hero_rect.height <= 0:
		hero_rect.y = 700
	screen.blit(bg, (0, 0))
	screen.blit(hero, hero_rect)
	pygame.display.update()
	#退出
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()
			exit()

	enemy_group.update()
	enemy_group.draw(screen)

	pygame.display.update()

pygame.quit()


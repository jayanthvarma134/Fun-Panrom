import pygame
import random
#initialize pygame
pygame.init()

#creatint screen 
screen = pygame.display.set_mode((800, 600))

#Title
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spritesandimages/icon.png')
pygame.display.set_icon(icon)

#background
background_img = pygame.image.load('spritesandimages/background_set.png')

#Player
player_img = pygame.image.load('spritesandimages/space_ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemy_img = pygame.image.load('spritesandimages/enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(20, 200)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
	screen.blit(player_img, (x, y))

def enemy(x, y):
	screen.blit(enemy_img, (x, y)) 

#Game Loop
running = True
while  running:
	#screen colour
	screen.fill((0, 0, 0))
	screen.blit(background_img, (0,0))

	for events in pygame.event.get():

		if events.type == pygame.QUIT:
			running = False

		#keystrokes 
		if events.type == pygame.KEYDOWN:
			if events.key == pygame.K_LEFT:
				playerX_change = -0.3
			if events.key == pygame.K_RIGHT:
				playerX_change = 0.3
		if events.type == pygame.KEYUP:
			if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX = playerX + playerX_change
	if playerX < 0 :
		playerX = 0
	if playerX > 736 :
		playerX = 736

	enemyX = enemyX + enemyX_change
	if enemyX < 0 :
		enemyY += enemyY_change
		enemyX_change = 0.3
	if enemyX > 736 :
		enemyY += enemyY_change
		enemyX_change = -0.3

	enemy(enemyX, enemyY)
	player(playerX, playerY)
	pygame.display.update()


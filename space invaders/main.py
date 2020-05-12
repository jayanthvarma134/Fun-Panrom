import pygame
import random
import math
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

score = 0
 
#bullet 
bullet_img = pygame.image.load('spritesandimages/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

#Player
player_img = pygame.image.load('spritesandimages/space_ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemy_img = pygame.image.load('spritesandimages/enemy.png')
enemyX = random.randint(0,736)
enemyY = random.randint(20, 200)
enemyX_change = 5
enemyY_change = 40

def player(x, y):
	screen.blit(player_img, (x, y))

def enemy(x, y):
	screen.blit(enemy_img, (x, y)) 

def fire_bullet(x, y):
	global bullet_state
	bullet_state ='fire'
	screen.blit(bullet_img, (x+16, y+10))

def is_Collision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt(math.pow(enemyX-bulletX, 2) + pow(enemyY-bulletY, 2))
	if distance <= 27 :
		return True
	else :
		return False

#Game Loop
running = True
while running:
	#screen colour
	#screen.fill((0, 0, 0))
	screen.blit(background_img, (0,0))

	for events in pygame.event.get():

		if events.type == pygame.QUIT:
			running = False

		#keystrokes 
		if events.type == pygame.KEYDOWN:
			if events.key == pygame.K_LEFT:
				playerX_change = -5
			if events.key == pygame.K_RIGHT:
				playerX_change = 5
			if events.key == pygame.K_UP: 
				if bullet_state is 'ready':
					bullet_state = 'fire'
					bulletX= playerX

		if events.type == pygame.KEYUP:
			if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
				playerX_change = 0

	if bullet_state is 'fire':
		bulletY -= bulletY_change
		fire_bullet(bulletX, bulletY)
	if bulletY <= 0:
		bulletY = 480
		bullet_state = 'ready'

	playerX = playerX + playerX_change
	if playerX < 0 :
		playerX = 0
	if playerX > 736 :
		playerX = 736

	enemyX = enemyX + enemyX_change
	if enemyX < 0 :
		enemyY += enemyY_change
		enemyX_change = 5
	if enemyX > 736 :
		enemyY += enemyY_change
		enemyX_change = -5

	collision = is_Collision(enemyX, enemyY, bulletX, bulletY)
	if collision :
		bulletY = 480
		bullet_state = 'ready'
		score += 1
		enemyX = random.randint(0,736)
		enemyY = random.randint(20, 200)
		print(score)

	enemy(enemyX, enemyY)
	player(playerX, playerY)
	pygame.display.update()


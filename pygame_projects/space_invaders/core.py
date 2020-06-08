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

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y) :
	score_val = font.render("Score : " + str(score), True, (255,255,255))
	screen.blit(score_val, (x,y))
 
#bullet 
number_of_strikes = 0
number_of_bullets = 150
bullet_img =[]
bulletX = []
bulletY = []
bulletX_change = []
bulletY_change = []
bullet_state = []

for i in range(number_of_bullets):
	bullet_state.append('ready')

#Player
player_img = pygame.image.load('spritesandimages/space_ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
num_of_enemies = 5
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change =[]
enemyY_change=[]
left_right = [-1,1]

for i in range(num_of_enemies):
	enemy_img.append(pygame.image.load('spritesandimages/enemy.png'))
	enemyX.append(random.randint(0,736))
	enemyY.append(random.randint(20, 200))
	enemy_left_right = random.choice(left_right)
	enemyX_change.append(5*enemy_left_right)
	enemyY_change.append(40)

def player(x, y):
	screen.blit(player_img, (x, y))

def enemy(x, y, i):
	screen.blit(enemy_img[i], (x, y)) 

def fire_bullet(x, y, j):
	global bullet_state
	bullet_state[j] ='fire'
	screen.blit(bullet_img[j], (x+16, y+10))

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

	#bullets emerging in dynamic real time
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
				number_of_strikes +=1
				bullet_img.append(pygame.image.load('spritesandimages/bullet.png'))
				bulletX.append(0)
				bulletY.append(480)
				bulletX_change.append(0)
				bulletY_change.append(10)
				#bullet_state.append('ready')
				for j in range(number_of_strikes):
					if bullet_state[j] is 'ready':
						bullet_state[j] = 'fire'
						bulletX[j]= playerX

		if events.type == pygame.KEYUP:
			if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
				playerX_change = 0

	for j2 in range(number_of_strikes) :
		if bullet_state[j2] is 'fire':
			bulletY[j2] -= bulletY_change[j2]
			fire_bullet(bulletX[j2], bulletY[j2], j2)
		'''if bulletY[j] <= 0:
			bulletY[j] = 480
			bullet_state[j] = ('ready')'''

	playerX = playerX + playerX_change
	if playerX < 0 :
		playerX = 0
	if playerX > 736 :
		playerX = 736

	for i in range(num_of_enemies):
		enemyX[i] = enemyX[i] + enemyX_change[i]
		if enemyX[i] < 0 :
			enemyY[i] += enemyY_change[i]
			enemyX_change[i] = 5
		if enemyX[i] > 736 :
			enemyY[i] += enemyY_change[i]
			enemyX_change[i] = -5
		for j3 in range(number_of_strikes):
			collision = is_Collision(enemyX[i], enemyY[i], bulletX[j3], bulletY[j3])
			if collision :
				bulletY[j3] = 480
				bullet_state[j3] = 'ready'
				score += 1
				enemyX[i] = random.randint(0,736)
				enemyY[i] = random.randint(20, 200)
				print(score)

		enemy(enemyX[i], enemyY[i], i)

	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()


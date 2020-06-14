import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox

pygame.init()

class cube():
	def __init__(self, position, color = (255, 0, 0)):
		self.pos = position
		self.dirx= 1
		self.diry = 0
		self.color = color
	def move(self, dirx, diry):
		self.dirx = dirx
		self.diry = diry
		self.pos = (self.pos[0]+self.dirx, self.pos[1]+self.diry)
	def  draw(self, surface, eyes = False):
		dis = block_size
		i= self.pos[0]
		j = self.pos[1]
		pygame.draw.rect(surface, self.color, (i*dis + 1, j*dis +1, dis -2, dis -2) )
		if eyes:
			center = dis//2
			radius = 3
			circleMiddle = (i*dis +center - radius, j*dis + 8)
			circleMiddle2 = (i*dis + dis - radius*2, j*dis + 8)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
			pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake():
	body = []
	turns = {}
	def __init__(self, position):
		self.color = (255,0,0)
		self.pos = position
		self.head = cube(self.pos)
		self.body.append(self.head)
		self.dirx = 0 
		self.diry = 1
	def move(self):
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				pygame.quit()
			keys = pygame.key.get_pressed()
			for key in keys:

				if keys[pygame.K_LEFT]:
					self.dirx = -1
					self.diry = 0
					self.turns[self.head.pos[:]]= [self.dirx, self.diry]
				elif keys[pygame.K_RIGHT]:
					self.dirx = 1
					self.diry = 0
					self.turns[self.head.pos[:]]= [self.dirx, self.diry]

				elif keys[pygame.K_UP]:
					self.dirx = 0
					self.diry = -1
					self.turns[self.head.pos[:]]= [self.dirx, self.diry]

				elif keys[pygame.K_DOWN]:
					self.dirx = 0
					self.diry = 1
					self.turns[self.head.pos[:]]= [self.dirx, self.diry]

		for i, c in enumerate(self.body):
			p = c.pos[:]
			if c.dirx == -1 and c.pos[0]<=0 :
				c.pos = (rows -1, c.pos[1])
			elif c.dirx == 1 and c.pos[0]>= rows -1:
				c.pos = (0, c.pos[1])
			elif c.diry == -1 and c.pos[1]<=0 :
				c.pos = (c.pos[0], rows-1)
			elif c.diry == 1 and c.pos[1]>=rows-1 :
				c.pos = (c.pos[0], 0)
			else:
				if p in self.turns:
					turn =  self.turns[p]
					c.move(turn[0], turn[1])
					if i == len(self.body)-1:
						self.turns.pop(p)
				else:
					c.move(c.dirx, c.diry)

	def add_cube(self):
		tail = self.body[-1]

		if tail.dirx == -1 and tail.diry == 0:
			self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
		if tail.dirx == 1 and tail.diry == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
		if tail.dirx == 0 and tail.diry == -1:
			self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
		if tail.dirx == 0 and tail.diry == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]-1)))

		self.body[-1].dirx = tail.dirx
		self.body[-1].diry = tail.diry

	def draw(self, surface):
		for i, c in enumerate(self.body):
			if i ==0 :
				c.draw(surface, True)
			else:
				c.draw(surface)

def random_snack(item):
	positions = item.body
	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda z:z.pos == (x,y),positions)))>0:
			continue
		else:
			break
	return (x,y)

def draw_grid(window_):
	x=0
	y=0
	for i in range(block_size):
		pygame.draw.line((window_), (255, 255, 255), (x,0),(x,width))
		pygame.draw.line((window_), (255,255,255), (0,y),(width,y))
		x+= block_size
		y+= block_size
	# drawing a line for the closing boundary 
	'''pygame.draw.line((window_), (255, 255, 255), (499,0),(499, 499))
	pygame.draw.line((window_), (255, 255, 255), (0,499),(499, 499))'''

def update_win(window_):
	window_.fill((0,0,0))
	draw_grid(window_)
	s.draw(window_)
	snack.draw(window_)
	pygame.display.update()

def main():
	global width, rows, block_size, s, snack
	width = 500
	rows = 20
	block_size = width//rows
	window = pygame.display.set_mode((width, width))
	s = snake((1,10))
	snack = cube(random_snack(s), color = (0, 255, 0))
	#clock = pygame.time.Clock()
	run = True
	while(run):
		pygame.time.delay(150)
		#clock.tick(10)
		if s.body[0].pos == snack.pos:
			s.add_cube()
			snack = cube(random_snack(s), color = (0, 255, 0))
		update_win(window)
		s.move()


main()

import pygame
import numpy 
import random



class cube():
	pass

class snake():
	pass

def draw_grid():
	pass

def update_win(window_):
	window_.fill((255, 255, 255))
	pygame.display.update()

def main():
	width = 500
	window = pygame.display.set_mode((width, width))
	run = True
	while(run):
		update_win(window)
		for keys in pygame.event.get():
			if keys.type == pygame.QUIT:
				run = False



main()

import pygame
from pygame.locals import *
from macgyver import MacGyver
import ressource
import os

class Labyrinth:

	def __init__(self, screen):
		
		self.position = {}

		with open("labyrinth.txt", "r") as f:
			row = 0
			for y in f:
				column = 0
				for x in y:
					self.position[(row, column)] = x
					column += 1
				row += 1


	def display(self, screen):
		for key, value in self.position.items():
			x = key[0] * 20
			y = key[1] * 20
			if value == "X":
				walls = pygame.image.load('wall.bmp').convert()
				pygame.display.update()
				screen.blit(walls, (x, y))
				pygame.display.flip()


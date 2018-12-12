import pygame

from pygame.locals import *

import ressource

from macgyver import MacGyver
from items import Items


class Labyrinth:

	def __init__(self, screen):
		
		self.position = {}

		# Every sprite has an x and a y as key
		with open("laby.txt", "r") as f:
			row = 0
			for y in f:
				column = 0
				for x in y:
					self.position[(column, row)] = x
					column += 1
				row += 1

		# Adds the 3 items on the labyrinthe structure
		random_items = Items(self.position, self)


	def display(self, screen):

		# Convert position in pixels
		for key, value in self.position.items():
			x = key[0] * 40
			y = key[1] * 40

			# Fill sprite with an image
			if value == "X":
				walls = pygame.image.load('ressource/wall.png').convert()
				pygame.display.update()
				screen.blit(walls, (x, y))
				pygame.display.flip()

			elif value == "T":
				tube = pygame.image.load('ressource/tube3.png').convert()
				pygame.display.update()
				screen.blit(tube, (x, y))
				pygame.display.flip()

			elif value == "E":
				ether = pygame.image.load('ressource/ether2.png').convert()
				pygame.display.update()
				screen.blit(ether, (x, y))
				pygame.display.flip()

			elif value == "N":
				needle = pygame.image.load('ressource/needle.png').convert()
				pygame.display.update()
				screen.blit(needle, (x, y))
				pygame.display.flip()

			elif value == "A":
				guardian = pygame.image.load('ressource/Guardian2.png').convert()
				pygame.display.update()
				screen.blit(guardian, (x, y))
				pygame.display.flip()




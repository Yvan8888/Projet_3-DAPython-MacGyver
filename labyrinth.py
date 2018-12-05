import pygame
from pygame.locals import *
from macgyver import MacGyver
import ressource
import os
from items import Items

class Labyrinth:

	def __init__(self, screen):
		
		self.position = {}

		with open("laby.txt", "r") as f:
			row = 0
			for y in f:
				column = 0
				for x in y:
					self.position[(row, column)] = x
					column += 1
				row += 1

		random_items = Items(self.position, self)


	def display(self, screen):
		for key, value in self.position.items():
			x = key[1] * 40
			y = key[0] * 40
			if value == "X":
				walls = pygame.image.load('ressource/Gardien.png').convert()
				pygame.display.update()
				screen.blit(walls, (x, y))
				pygame.display.flip()

			elif value == "T":
				tube = pygame.image.load('ressource/MacGyver.png').convert()
				pygame.display.update()
				screen.blit(tube, (x, y))
				pygame.display.flip()

			elif value == "E":
				ether = pygame.image.load('ressource/MacGyver.png').convert()
				pygame.display.update()
				screen.blit(ether, (x, y))
				pygame.display.flip()

			elif value == "N":
				needle = pygame.image.load('ressource/MacGyver.png').convert()
				pygame.display.update()
				screen.blit(needle, (x, y))
				pygame.display.flip()

"""			elif value == "S":
				macgyver = pygame.image.load('ressource/Macgyver.png').convert()
				pygame.display.update()
				screen.blit(macgyver, (x, y))
				pygame.display.flip()
"""






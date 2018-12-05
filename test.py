"""import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode([640, 400])

red = (230,50,50)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

	window.fill((40,50,180))
	pygame.draw.rect(window, (red), Rect((100,300), (10,30)))

	pygame.display.update()

"""

import pygame
from pygame.locals import *
from macgyver import MacGyver

class Labyrinth:

	#def __init__(self):
		
		position = {}

		with open("labyrinth.txt", "r") as f:
			row = 0
			for y in f:
				column = 0
				for x in y:
					position[(row, column)] = x
					column += 1
				row += 1
"""
		def display(self, screen):
		color2 = (230, 50, 50)
		for i in self.position:
			if i == "X":
				row = self.position.index(i) + 1
				column = self.position.index(i) + 2
				x = self.position[row] * 20
				y = self.position[column] * 20

			walls = pygame.image.load('wall.png')
			pygame.display.update()
"""
l = Labyrinth()
print(l.position)


"""



"""



import pygame
from pygame.locals import *
from labyrinth import Labyrinth
from macgyver import MacGyver


class Main:

	def __init__(self):
		pygame.init()

		self.size = width, height = 600, 600

		self.title = pygame.display.set_caption("Labyrinth")

		self.screen = pygame.display.set_mode(self.size)
		pygame.display.flip()

		self.background = pygame.Surface(self.size)

		self.screen.blit(self.background,(0,0))

		self.labyrinth = Labyrinth(self.screen)
		self.macgyver = MacGyver(self.screen)

	def loop(self):

		done = False
		while not done:

			self.labyrinth.display(self.screen)
			pygame.display.flip()

			for event in pygame.event.get():

				if event.type == KEYDOWN:
#					self.macgyver.collide(self.labyrinth, position)
					if event.key == K_RIGHT:
						self.macgyver.move_right(self.screen)

					elif event.key == K_LEFT:
						self.macgyver.move_left(self.screen)

					elif event.key == K_UP:
						self.macgyver.move_up(self.screen)

					elif event.key == K_DOWN:
						self.macgyver.move_down(self.screen)

				if event.type == pygame.QUIT:
					done = True

		pygame.quit()

#		while True:
#			self.labyrinth.display(self.screen)
#			pygame.display.flip()

	def collecting_items(self):
		for key, value in self.position.items():
			x = key[0] * 20
			y = key[1] * 20
			if value == "E" and self.macgyver.position.get((x, y)) == "E":
				add_item_to_backpack("Ether")

			elif value == "N" and self.macgyver.position.get((x, y)) == "N":
				add_item_to_backpack("Needle")

			elif value == "T" and self.macgyver.position.get((x, y)) == "T":
				add_item_to_backpack("Tube")

		if len(backpack) == 3:
			print('All items are collected, you can face the guardian.')

		elif len(backpack) == 2:
			print('Only 1 item is missing.')

		elif len(backpack) == 1:
			print('Go on! 2 items left.')



if __name__ == '__main__':
	main = Main()
	main.loop()








"""
class Labyrinth
	Hauteur
	Largeur
	Départ
	Arrivée
	Emplacement des murs

	Init

class Position
	Latitude
	Longitude

	Init

class MacGyver
	Position départ
	Nombre de magicitems

	Init
	Se déplacer
	Récupérer les magicitems
	Mourir
	Endormir


class Watchman
	Position

	Init
	Tuer
	S'endormir


class MagicItems
	Emplacement aléatoire

	Init
	Changer d'emplacements


MacGiver se déplace sur le Labyrinth
Watchman est le labyrinth
MagicItems sont sur le labyrinth

"""























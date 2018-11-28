import pygame
from pygame.locals import *
from labyrinth import Labyrinth
from macgyver import MacGyver


class Main:

	def __init__(self):
		pygame.init()

		self.size = width, height = 300, 300

		self.title = pygame.display.set_caption("Labyrinth")

		self.screen = pygame.display.set_mode(self.size)
		pygame.display.flip()

		self.background = pygame.Surface(self.size)

		self.screen.blit(self.background,(0,0))

		self.labyrinth = Labyrinth(self.screen)



	def collide(self):
		pass

	def loop(self):
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True

		pygame.quit()

		while True:
			self.labyrinth.display(self.screen)
			pygame.display.flip()

	def move(self):
		macgyver = MacGyver()
		macgyver.move_right()
		macgyver.move_left()
		macgyver.move_up()
		macgyver.move_down()

		while True:
			for event in pygame.event.get():

				if event.type==KEYDOWN:
					if event.key == K_RIGHT:
						self.labyrinth.move_right()

					elif event.key == K_LEFT:
						self.labyrinth.move_left()

					elif event.key == K_UP:
						self.labyrinth.move_up()

					elif event.key == K_DOWN:
						self.labyrinth.move_down()



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























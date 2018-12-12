import pygame

from pygame.constants import KEYDOWN, QUIT, K_RIGHT, K_LEFT, K_UP, K_DOWN

from labyrinth import Labyrinth
from macgyver import MacGyver


class Main:
	"""
	g
	"""
	def __init__(self):
		pygame.init()

		self.size = 600, 700

		self.title = pygame.display.set_caption("Labyrinth")

		self.screen = pygame.display.set_mode(self.size)
		pygame.display.flip()

		self.background = pygame.Surface(self.size)

		self.screen.blit(self.background,(0,0))

		# Create the labyrinth.
		self.labyrinth = Labyrinth(self.screen)

		# Create the player.
		self.macgyver = MacGyver(self.screen, self.labyrinth)

		self.information()

	def information(self):
		font = pygame.font.SysFont("monospace", 17)

		instructions = font.render(
					"After having picked up all the items, you can face the guardian",
					1, 
					(255, 255, 255))
		self.screen.blit(instructions, (20, 620))

		backpack = font.render("Your backpack contains: ", 1, (255, 255, 255))
		self.screen.blit(backpack, (40, 640))

	def loop(self):

		# Display labyrinth on the screen and allow for updates.
		self.labyrinth.display(self.screen)
		pygame.display.flip()

		# Allow to move MacGyver
		done = False
		while not done:

			for event in pygame.event.get():

				if event.type == KEYDOWN:
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

if __name__ == '__main__':
	main = Main()
	main.loop()

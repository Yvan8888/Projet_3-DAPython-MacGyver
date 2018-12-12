import pygame
import os

from pygame.locals import *


class MacGyver:

	def __init__(self, screen, labyrinth):

		# Initial position.
		self.x = 40
		self.y = 40

		# MacGyver moves from one sprite to another.
		self.speed = 40

		# Store the items picked up.
		self.backpack = []

		self.labyrinth = labyrinth

		# Display MacGyver on the screen.
		self.player = pygame.image.load(os.path.join('Ressource', 'MacGyver2.png')).convert()
		screen.blit(self.player, (self.x, self.y))
		pygame.display.update()

	def move_macgyver(self, screen):

		# Display MacGyver on the screen in its new position;
		screen.blit(self.player, (self.x, self.y))
		pygame.display.update()

	def win(self, screen):
		font = pygame.font.SysFont("monospace", 100)

		lab = font.render("Victory !" , 1, (255, 255, 255))
		screen.blit(lab, (180, 300))
		pygame.display.update()

	def lose(self, screen):
		font = pygame.font.SysFont("monospace", 100)

		lab = font.render("Game over", 1, (255, 255, 255))
		screen.blit(lab, (140, 300))
		pygame.display.update()

	def show_backpack(self, screen):

		# This function displays what the backpack contains.
		bp = self.backpack

		if "N" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label3 = font.render("1 Needle", 1, (255, 255, 255))
			screen.blit(label3, (180, 640))

		if "E" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label4 = font.render("1 Ether", 1, (255, 255, 255))
			screen.blit(label4, (230, 640))

		if "T" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label5 = font.render("1 Tube", 1, (255, 255, 255))
			screen.blit(label5, (280, 640))

		if "E" in bp and "T" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label6 = font.render("1 item left", 1, (255, 255, 255))
			screen.blit(label6, (180, 680))
		elif "E" in bp and "N" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label6 = font.render("1 item left", 1, (255, 255, 255))
			screen.blit(label6, (180, 680))
		elif "N" in bp and "T" in bp:
			font = pygame.font.SysFont("monospace", 17)
			label6 = font.render("1 item left", 1, (255, 255, 255))
			screen.blit(label6, (180, 680))

		if "E" in bp and "N" in bp and "T" in bp:
			screen.fill((0,0,0), (0, 600, 600, 100))
			font = pygame.font.SysFont("monospace", 17)
			label7 = font.render(
						"You have everything you need in your backpack, let's face the guardian !", 
						1, 
						(255, 255, 255))
			screen.blit(label7, (140, 640))

		pygame.display.update()

	def collide(self, dest):

		# Return new position of MacGyver
		return self.labyrinth.position[dest]

	def add_item_to_backpack(self, item):
		self.backpack.append(item)

	def move_right(self, screen):

		# Take the new position
		make_the_move = self.collide((self.x // 40 + 1, self.y // 40))

		if make_the_move == " ":

			# Erase MacGyver in its position before the move
			x = self.x
			screen.fill((0,0,0), (x, self.y, 40, 40))

			self.x += self.speed
			self.move_macgyver(screen)

		elif make_the_move == "E" or make_the_move == "T" or make_the_move == "N":
			if make_the_move not in self.backpack:
				self.add_item_to_backpack(make_the_move)

			x = self.x
			screen.fill((0,0,0), (x, self.y, 40, 40))

			self.x += self.speed
			self.move_macgyver(screen)

			# Updates backpack display
			self.show_backpack(screen)

	def move_left(self, screen):
		make_the_move = self.collide((self.x // 40 - 1, self.y // 40))

		if make_the_move == " " or make_the_move == "S":
			x = self.x
			screen.fill((0,0,0), (x, self.y, 40, 40))

			self.x -= self.speed
			self.move_macgyver(screen)

		elif make_the_move == "E" or make_the_move == "T" or make_the_move == "N":
			if make_the_move not in self.backpack:
				self.add_item_to_backpack(make_the_move)

			x = self.x
			screen.fill((0,0,0), (x, self.y, 40, 40))

			self.x -= self.speed
			self.move_macgyver(screen)

			self.show_backpack(screen)

	def move_up(self, screen):
		make_the_move = self.collide((self.x // 40, self.y // 40 - 1))

		if make_the_move == " " or make_the_move == "S":
			y = self.y
			screen.fill((0,0,0), (self.x, y, 40, 40))

			self.y -= self.speed
			self.move_macgyver(screen)

		elif make_the_move == "E" or make_the_move == "T" or make_the_move == "N":
			if make_the_move not in self.backpack:
				self.add_item_to_backpack(make_the_move)

			y = self.y
			screen.fill((0,0,0), (self.x, y, 40, 40))

			self.y -= self.speed
			self.move_macgyver(screen)

			self.show_backpack(screen)

		if make_the_move == "A" and len(self.backpack) == 3:
			y = self.y
			screen.fill((0,0,0), (self.x, y, 40, 40))
			self.y -= self.speed
			self.move_macgyver(screen)
		elif make_the_move == "A" and len(self.backpack) != 3:
			self.lose(screen)

		final_position = self.collide((self.x // 40, self.y // 40))
			
		if final_position == "A":
			self.win(screen)


	def move_down(self, screen):
		make_the_move = self.collide(((self.x) // 40, self.y // 40 + 1))

		if make_the_move == " ":
			y = self.y
			screen.fill((0,0,0), (self.x, y, 40, 40))

			self.y += self.speed
			self.move_macgyver(screen)

		elif make_the_move == "E" or make_the_move == "T" or make_the_move == "N":
			if make_the_move not in self.backpack:
				self.add_item_to_backpack(make_the_move)

			y = self.y
			screen.fill((0,0,0), (self.x, y, 40, 40))

			self.y += self.speed
			self.move_macgyver(screen)

			self.show_backpack(screen)




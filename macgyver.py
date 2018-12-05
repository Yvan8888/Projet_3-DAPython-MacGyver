import pygame

class MacGyver:

	def __init__(self, screen):
		self.x = 40
		self.y = 40
		self.speed = 40
		self.backpack = []
		self.player = pygame.image.load('Ressource/MacGyver.png').convert()
		screen.blit(self.player, (self.x, self.y))
		pygame.display.update()

	def move_macgyver(self, screen):
		screen.blit(self.player, (self.x, self.y))
		pygame.display.update()

	def move_right(self, screen):
		x = self.x
		screen.fill((0,0,0), (x, self.y, 40, 43))
		self.x += self.speed
		self.move_macgyver(screen)

	def move_left(self, screen):
		x = self.x
		screen.fill((0,0,0), (x, self.y, 40, 43))
		self.x -= self.speed
		self.move_macgyver(screen)

	def move_up(self, screen):
		y = self.y
		screen.fill((0,0,0), (self.x, y, 40, 43))
		self.y -= self.speed
		self.move_macgyver(screen)

	def move_down(self, screen):
		y = self.y
		screen.fill((0,0,0), (self.x, y, 40, 43))
		self.y += self.speed
		self.move_macgyver(screen)

	def collide(self, labyrinth, position):
		x = self.x
		y =	self.y

		if labyrinth.position[(x, y)] == "X":
			x = self.x
			y = self.y

		elif labyrinth.position[(x, y)] == " ":
			labyrinth.position[(x, y)] = "S"

	def add_item_to_backpack(self, item):
		self.backpack.append(item)






























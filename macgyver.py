

class MacGyver:

	def __init__(self):
		self.x = 1
		self.y = 1
		self.speed = 1
		self.backpack = []



	def move_right(self):
		self.x += self.speed

	def move_left(self):
		self.x -= self.speed

	def move_up(self):
		self.y -= self.speed

	def move_down(self):
		self.y += self.speed

	def add_items_to_backpack(self):
		pass
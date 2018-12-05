import random

class Items:

	def __init__(self, position, labyrinth):

		self.x = 0
		self.y = 0

		self.random_position(position, labyrinth)

	def random_position(self, position, labyrinth):

		items_available = ['E', 'N', 'T']

		for i in range(3):

			done = False

			while not done:
				self.x = random.randint(0, 15)
				self.y = random.randint(0, 15)

				if labyrinth.position[(self.x, self.y)] == " ":
					labyrinth.position[(self.x, self.y)] = random.choice(items_available)
#					items_available.remove(assign_item)
					done = True







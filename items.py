"""
Item
"""
import random


class Items:
    """
    Generate and assign a random position to the 3 items.
    """

    def __init__(self, labyrinth):

        self.i_x = 0
        self.i_y = 0

        self.random_position(labyrinth)

    def random_position(self, labyrinth):
        """
        Gives a random position to the 3 items.
        """
        items_available = ['E', 'N', 'T']

        while items_available != []:

            done = False
            while not done:
                self.i_x = random.randint(0, 14)
                self.i_y = random.randint(0, 14)

                if labyrinth.position[(self.i_x, self.i_y)] == " ":
                    labyrinth.position[(self.i_x, self.i_y)] = random.choice(items_available)
                    assign_item = labyrinth.position[(self.i_x, self.i_y)]
                    items_available.remove(assign_item)
                    done = True

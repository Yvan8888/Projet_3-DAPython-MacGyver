"""
Labyrinth
"""
import pygame

from items import Items


class Labyrinth:
    """
    Create labyrinth in a dictionary and display it.
    """

    def __init__(self):

        self.position = {}

        # Every sprite has an x and a y as key.
        with open("laby.txt", "r") as file:
            row = 0
            for file_y in file:
                column = 0
                for file_x in file_y:
                    self.position[(column, row)] = file_x
                    column += 1
                row += 1

        # Adds the 3 items on the labyrinthe structure.
        self.random_items = Items(self)

    def display(self, screen):
        """
        For every caracter in laby.txt, an image is displayed.
        """

        # Convert position in pixels
        for key, value in self.position.items():
            d_x = key[0] * 40
            d_y = key[1] * 40

            # Fill sprite with an image.
            if value == "X":
                walls = pygame.image.load('ressource/wall.png').convert()
                pygame.display.update()
                screen.blit(walls, (d_x, d_y))
                pygame.display.flip()

            elif value == "T":
                tube = pygame.image.load('ressource/tube3.png').convert()
                pygame.display.update()
                screen.blit(tube, (d_x, d_y))
                pygame.display.flip()

            elif value == "E":
                ether = pygame.image.load('ressource/ether2.png').convert()
                pygame.display.update()
                screen.blit(ether, (d_x, d_y))
                pygame.display.flip()

            elif value == "N":
                needle = pygame.image.load('ressource/needle.png').convert()
                pygame.display.update()
                screen.blit(needle, (d_x, d_y))
                pygame.display.flip()

            elif value == "A":
                guardian = pygame.image.load('ressource/Guardian2.png').convert()
                pygame.display.update()
                screen.blit(guardian, (d_x, d_y))
                pygame.display.flip()

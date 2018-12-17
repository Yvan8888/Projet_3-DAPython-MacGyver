"""
Welcome to this labyrinth
"""
import pygame

from pygame.constants import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE

from labyrinth import Labyrinth
from macgyver import MacGyver


class Main:
    """
    Main class handles labyrinth set up,
    display of informations,
    and how to move macgyver.
    """
    def __init__(self):
        pygame.init()

        self.size = 600, 700

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.flip()

        self.title = pygame.display.set_caption("Labyrinth")

        self.background = pygame.Surface(self.size)

        self.screen.blit(self.background, (0, 0))

        # Create the labyrinth.
        self.labyrinth = Labyrinth()

        # Create the player.
        self.macgyver = MacGyver(self.screen, self.labyrinth)

        self.information()

    def information(self):
        """
        Display useful informaton below the labyrinth.
        """

        font = pygame.font.SysFont("monospace", 17)

        instructions = font.render(
            "After having picked up all the items, you can face the guardian",
            1,
            (255, 255, 255))
        self.screen.blit(instructions, (20, 620))

        backpack = font.render("Your backpack contains: ", 1, (255, 255, 255))
        self.screen.blit(backpack, (40, 640))

    def loop(self):
        """
        How to move macgyver.
        """

        # Display labyrinth on the screen and allow for updates.
        self.labyrinth.display(self.screen)
        pygame.display.flip()

        # Allow to move MacGyver
        done = False
        done2 = False
        while not done:

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    make_the_move = ""

                    if event.key == K_RIGHT:
                        make_the_move = self.macgyver.collide((
                            self.macgyver.mc_x // 40 + 1,
                            self.macgyver.mc_y // 40))
                        self.macgyver.move(self.screen, "right", make_the_move)

                    elif event.key == K_LEFT:
                        make_the_move = self.macgyver.collide((
                            self.macgyver.mc_x // 40 - 1,
                            self.macgyver.mc_y // 40))
                        self.macgyver.move(self.screen, "left", make_the_move)

                    elif event.key == K_UP:
                        make_the_move = self.macgyver.collide((
                            self.macgyver.mc_x // 40,
                            self.macgyver.mc_y // 40 - 1))
                        self.macgyver.move(self.screen, "up", make_the_move)


                    elif event.key == K_DOWN:
                        make_the_move = self.macgyver.collide((
                            self.macgyver.mc_x // 40,
                            self.macgyver.mc_y // 40 + 1))
                        self.macgyver.move(self.screen, "down", make_the_move)

                    final_position = self.macgyver.collide((
                        self.macgyver.mc_x // 40,
                        self.macgyver.mc_y // 40))

                    # When game is over, not able to move around anymore.
                    if make_the_move == "A":
                        done = True

                    # When game is won, not able to move around anymore.
                    if final_position == "A":
                        self.macgyver.win(self.screen)
                        done = True

                    # To quit the game.
                    if event.key == K_SPACE:
                        done = True
                        done2 = True

        while not done2:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done2 = True

        quit()

if __name__ == '__main__':
    MAIN = Main()
    MAIN.loop()

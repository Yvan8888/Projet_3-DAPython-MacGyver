"""
MacGyver
"""
import os
import pygame


class MacGyver:
    """
    This class is all about the player.
    """
    def __init__(self, screen, labyrinth):

        # Initial position.
        self.mc_x = 40
        self.mc_y = 40

        # MacGyver moves from one sprite to another.
        self.speed = 40

        # Store the items picked up.
        self.backpack = []

        self.labyrinth = labyrinth

        self.macgyver = pygame.image.load(os.path.join('Ressource', 'MacGyver2.png')).convert()
        pygame.display.update()
        screen.blit(self.macgyver, (self.mc_x, self.mc_y))
        pygame.display.flip()

    @classmethod
    def win(cls, screen):
        """
        Display a victory message.
        """
        font = pygame.font.SysFont("monospace", 100)

        lab = font.render("Victory !", 1, (255, 255, 255))
        screen.blit(lab, (180, 300))
        pygame.display.update()

    @classmethod
    def lose(cls, screen):
        """
        Display a game over message.
        """
        font = pygame.font.SysFont("monospace", 100)

        lab = font.render("Game over", 1, (255, 255, 255))
        screen.blit(lab, (140, 300))
        pygame.display.update()

    def show_backpack(self, screen):
        """
        This function displays what the backpack contains.
        """
        if "N" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label3 = font.render("1 Needle", 1, (255, 255, 255))
            screen.blit(label3, (180, 640))

        if "E" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label4 = font.render("1 Ether", 1, (255, 255, 255))
            screen.blit(label4, (230, 640))

        if "T" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label5 = font.render("1 Tube", 1, (255, 255, 255))
            screen.blit(label5, (280, 640))

        if "E" in self.backpack and "T" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label6 = font.render("1 item left", 1, (255, 255, 255))
            screen.blit(label6, (180, 680))
        elif "E" in self.backpack and "N" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label6 = font.render("1 item left", 1, (255, 255, 255))
            screen.blit(label6, (180, 680))
        elif "N" in self.backpack and "T" in self.backpack:
            font = pygame.font.SysFont("monospace", 17)
            label6 = font.render("1 item left", 1, (255, 255, 255))
            screen.blit(label6, (180, 680))

        if "E" in self.backpack and "N" in self.backpack and "T" in self.backpack:
            screen.fill((0, 0, 0), (0, 600, 600, 100))
            font = pygame.font.SysFont("monospace", 17)
            label7 = font.render(
                "You have everything you need in your backpack, let's face the guardian !",
                1,
                (255, 255, 255))
            screen.blit(label7, (140, 640))

        pygame.display.update()

    def collide(self, dest):
        """
        Return new position of MacGyver
        """
        return self.labyrinth.position[dest]

    def add_item_to_backpack(self, item):
        """
        Add a collected item to backpack.
        """
        self.backpack.append(item)

    def speed_affect(self, direction):
        """
        Affect a speed of one sprite
        """
        if direction == "right":
            self.mc_x += self.speed
        elif direction == "left":
            self.mc_x -= self.speed
        elif direction == "up":
            self.mc_y -= self.speed
        elif direction == "down":
            self.mc_y += self.speed

    def move(self, screen, direction, make_the_move):
        """
        Check what action to take depending on what is next on the path
        """
        if make_the_move in (" ", "S"):
            screen.fill((0, 0, 0), (self.mc_x, self.mc_y, 40, 40))

            self.speed_affect(direction)

            self.move_macgyver(screen)

        elif make_the_move in ("E", "T", "N"):
            if make_the_move not in self.backpack:
                self.add_item_to_backpack(make_the_move)

            screen.fill((0, 0, 0), (self.mc_x, self.mc_y, 40, 40))

            self.speed_affect(direction)

            self.move_macgyver(screen)
            self.show_backpack(screen)

        elif make_the_move == "A" and len(self.backpack) == 3:
            screen.fill((0, 0, 0), (self.mc_x, self.mc_y, 40, 40))

            self.speed_affect(direction)

            self.move_macgyver(screen)

        elif make_the_move == "A" and len(self.backpack) != 3:
            self.lose(screen)

    def move_macgyver(self, screen):
        """
        Display MacGyver on the screen in its new position;
        """
        screen.blit(self.macgyver, (self.mc_x, self.mc_y))
        pygame.display.update()

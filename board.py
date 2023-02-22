import pygame
import os
from pprint import pprint
from checker import Checker


class Board(pygame.sprite.Sprite):
    def __init__(self, board_size: int):
        super().__init__()

        self.image = pygame.image.load(os.getenv("BOARD_IMAGE", ""))
        self.image = pygame.transform.scale_by(self.image, board_size / self.image.get_width())

        self.rect = self.image.get_rect(topleft = (0, 0))
        self.board = self.init()
        pprint(self.board)

    def init(self):
        board = [[0]*8]*8

        for row in range(8):
            for col in range(8):
                pass

        return board


    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)

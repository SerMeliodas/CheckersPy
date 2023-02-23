import pygame
import os
import numpy as np

from pprint import pprint
from checker import Checker


class Board(pygame.sprite.Sprite):
    def __init__(self, board_size: int):
        super().__init__()

        self.checker_group = pygame.sprite.Group()

        self.image = pygame.image.load(os.getenv("BOARD_IMAGE", ""))
        self.image = pygame.transform.scale_by(
            self.image, board_size / self.image.get_width())

        self.rect = self.image.get_rect(topleft = (0, 0))
        self.board = self.init()
        pprint(self.board)

    def init(self):

        def create_checkers(row: int, col: int, board: list):
            if row % 2 == 0 and col % 2 == 0:
                board[row][col] = Checker((row, col), self.checker_group)
            if row % 2 != 0 and col % 2 != 0:
                board[row][col] = Checker((row, col), self.checker_group)

        board = np.zeros((8, 8), dtype=object)

        for row in range(8):
            for col in range(8):
                if row < 3:
                    create_checkers(row, col, board)
                
                if row > 4:
                    create_checkers(row, col, board)

        return board


    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)
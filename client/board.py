from ctypes import pythonapi
import pygame
import os
import numpy as np

from pprint import pprint
from checker import Checker


class Board(pygame.sprite.Sprite):
    def __init__(self, board_size: int):
        super().__init__()

        self.white_checkers = pygame.sprite.Group()
        self.black_checkers = pygame.sprite.Group()

        self.image = pygame.image.load(os.getenv("BOARD_IMAGE", ""))
        self.image = pygame.transform.scale_by(
            self.image, board_size / self.image.get_width())

        self.rect = self.image.get_rect(topleft = (0, 0))
        self.board = self.init()

    def init(self):

        def create_checkers(row: int, col: int, color, board):
            if row % 2 == 0 and col % 2 == 0:
                board[row][col] = Checker(color,
                                          (row, col), 
                                          self.white_checkers if color == 'white' else self.black_checkers)
            if row % 2 != 0 and col % 2 != 0:
                board[row][col] = Checker(color, 
                                          (row, col), 
                                          self.white_checkers if color == 'white' else self.black_checkers)
        board = np.zeros((8, 8), dtype=object)

        for row in range(8):
            for col in range(8):
                if row < 3:
                    create_checkers(row, col, 'white', board)

                if row > 4:
                    create_checkers(row, col, 'grey', board)

        return board


    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)

        self.white_checkers.draw(surface)
        self.black_checkers.draw(surface)

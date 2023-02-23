import pygame
import sys

from dotenv import load_dotenv
import os

from .board import Board


class Game:
    def __init__(self, width: int, height: int) -> None:
        load_dotenv()
        pygame.init()

        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)

        self.board = Board(self.size[0])

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.event_loop()

            self.board.draw()
            pygame.display.flip()

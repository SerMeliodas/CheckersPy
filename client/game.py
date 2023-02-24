import pygame
import sys

from dotenv import load_dotenv
from board import Board
from player import Player


class Game:
    def __init__(self, width: int, height: int) -> None:
        load_dotenv()
        pygame.init()

        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)

        self.board = Board(self.size[0])

        self.oponent = Player("white", self.board.white_checkers.sprites())
        self.main = Player("black", self.board.black_checkers.sprites())

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self.main.event_listen(event)


    def run(self):
        while True:
            self.event_loop()

            self.board.draw()
            pygame.display.flip()

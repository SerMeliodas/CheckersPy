import pygame
from checker import Checker


class Player:
    def __init__(self, color: str, checkers: list[Checker]):
        self.beated_checkers = 0
        self.color = color
        self.__checkers: None | list[Checker] = checkers

    @property
    def checkers(self):
        return self.__checkers

    @checkers.setter
    def checkers(self, checkers: list[Checker]):
        self.__checkers = checkers

    def event_listen(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            pass

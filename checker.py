import pygame


class Checker(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, group):
        super().__init__(groups=group)
        self.pos = pos
import pygame
import os


class Checker(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, group):
        super().__init__(group)
        self.pos = pos
        self.__cell_size = int(eval(os.getenv("CELL_SIZE", '')))
        self.image = pygame.Surface((self.__cell_size, self.__cell_size))
        self.rect = self.image.get_rect()
        self.rect.centery = self.__cell_size * (self.pos[0] + 1) - self.__cell_size / 2
        self.rect.centerx = self.__cell_size * (self.pos[1] + 1) - self.__cell_size / 2

        pygame.draw.circle(self.image, (255, 0, 0),
                           (self.__cell_size / 2, self.__cell_size / 2), 
                           self.__cell_size / 2 - 3)

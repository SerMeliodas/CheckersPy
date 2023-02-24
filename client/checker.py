import pygame
import os


class Checker(pygame.sprite.Sprite):
    def __init__(self, color: str, pos: tuple, group):
        super().__init__(group)
        self.pos = pos
        self.color = pygame.Color(color)

        self.__cell_size = int(eval(os.getenv("CELL_SIZE", '')))
        self.__cell_pading = int(os.getenv("CELL_PADING", '5'))

        self.image = pygame.Surface((self.__cell_size, self.__cell_size),
                                    pygame.SRCALPHA)

        self.rect = self.image.get_rect()

        self.rect.centery = self.__cell_size * (self.pos[0] + 1) - self.__cell_size / 2 + self.__cell_pading
        self.rect.centerx = self.__cell_size * (self.pos[1] + 1) - self.__cell_size / 2 + self.__cell_pading

        pygame.draw.circle(self.image,self.color,
                           (self.__cell_size / 2, self.__cell_size / 2), 
                           self.__cell_size / 2 - self.__cell_pading)

    def move(self):
        pass

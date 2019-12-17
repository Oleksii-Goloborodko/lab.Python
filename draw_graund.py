import pygame
import copy

from helper.colors import Colors

class DrawGraund:
    def draw_all(self):
        self.surf1 = pygame.Surface((509, 509))
        self.surf1.fill(Colors.BLACK)
        self.surf2 = pygame.Surface((167, 167))
        self.surf2.fill(Colors.WHITE)
        self.surf3 = pygame.Surface([509, 509], pygame.SRCALPHA, 32)
        self.surf3 = self.surf3.convert_alpha()

        self.rect1 = pygame.Rect((2, 2, 167, 167))
        self.rect2 = pygame.Rect((171, 2, 167, 167))
        self.rect3 = pygame.Rect((340, 2, 167, 167))
        self.rect4 = pygame.Rect((2, 171, 167, 167))
        self.rect5 = pygame.Rect((171, 171, 167, 167))
        self.rect6 = pygame.Rect((340, 171, 167, 167))
        self.rect7 = pygame.Rect((2, 340, 167, 167))
        self.rect8 = pygame.Rect((171, 340, 167, 167))
        self.rect9 = pygame.Rect((340, 340, 167, 167))

        self.rect_all = [self.rect1, self.rect2, self.rect3 ,self.rect4 ,self.rect5 ,self.rect6 ,self.rect7 ,self.rect8, self.rect9]

        for i in self.rect_all:
            self.surf1.blit(self.surf2, i)

        logical = self.logic_list.copy()
        for i in self.logic_list:
            if i == 1:
                j = logical.index(i)
                logical[j] = False
                pygame.draw.rect(self.surf3, Colors.YELLOW, self.rect_all[j])
            elif i == 2:
                j = logical.index(i)
                logical[j] = False
                pygame.draw.rect(self.surf3, Colors.GREEN, self.rect_all[j])

        self.gameWindow.blit(self.surf1, (0, 0))
        self.gameWindow.blit(self.surf3, (0, 0))
import pygame

from helper.colors import Colors
from draw_graund import DrawGraund
from  draw_elements import DrawElements
from bl import Bl

class StartGame:
    def __init__(self):
        self.FPS = 60
        self.W = 509
        self.H = 509

        pygame.init()
        self.clock = pygame.time.Clock()
        self.gameWindow = pygame.display.set_mode((self.W, self.H))
        self.gameWindow.fill((255, 255, 255))

        pygame.display.set_caption("Hello")

        self.ground = pygame.Rect(0, 0, 600, 600)
        self. ground_surf = pygame.Surface((self.W, self.H))

        self.logic_list = [False, False, False, False, False, False, False, False, False]
        self.now_clik = False

        pygame.display.update()

        while 1:
            self.gameWindow.fill(Colors.WHITE)
            DrawGraund.draw_all(self)

            pygame.display.update()
            victory_status = Bl.All_bl(self)
            if victory_status != False:
                print("Victory")
                exit()
            if victory_status == 4:
                print("Oll lose")
                exit()

            for i in pygame.event.get():

                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    self.click_position = i.pos
                    self.now_clik = DrawElements.NewElement(self)
                    pygame.display.update()
            self.clock.tick(self.FPS)


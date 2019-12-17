import pygame

class Such:
    def Sucher(self):
        if pygame.Rect.collidepoint(self.rect1, self.click_position[0], self.click_position[1]):
            return 0
        elif pygame.Rect.collidepoint(self.rect2, self.click_position[0], self.click_position[1]):
            return 1
        elif pygame.Rect.collidepoint(self.rect3, self.click_position[0], self.click_position[1]):
            return 2
        elif pygame.Rect.collidepoint(self.rect4, self.click_position[0], self.click_position[1]):
            return 3
        elif pygame.Rect.collidepoint(self.rect5, self.click_position[0], self.click_position[1]):
            return 4
        elif pygame.Rect.collidepoint(self.rect6, self.click_position[0], self.click_position[1]):
            return 5
        elif pygame.Rect.collidepoint(self.rect7, self.click_position[0], self.click_position[1]):
            return 6
        elif pygame.Rect.collidepoint(self.rect8, self.click_position[0], self.click_position[1]):
            return 7
        elif pygame.Rect.collidepoint(self.rect9, self.click_position[0], self.click_position[1]):
            return 8
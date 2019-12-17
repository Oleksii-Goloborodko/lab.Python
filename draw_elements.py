import pygame

from suchcher import Such

class DrawElements:
    def NewElement(self):
        if pygame.Rect.collidepoint(self.rect1, self.click_position[0], self.click_position[1]):
            print("True 1")
            if self.logic_list[0] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect2, self.click_position[0], self.click_position[1]):
            print("True 2")
            if self.logic_list[1] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect3, self.click_position[0], self.click_position[1]):
            print("True 3")
            if self.logic_list[2] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect4, self.click_position[0], self.click_position[1]):
            print("True 4")
            if self.logic_list[3] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect5, self.click_position[0], self.click_position[1]):
            print("True 5")
            if self.logic_list[4] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect6, self.click_position[0], self.click_position[1]):
            print("True 6")
            if self.logic_list[5] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect7, self.click_position[0], self.click_position[1]):
            print("True 7")
            if self.logic_list[6] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect8, self.click_position[0], self.click_position[1]):
            print("True 8")
            if self.logic_list[7] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        elif pygame.Rect.collidepoint(self.rect9, self.click_position[0], self.click_position[1]):
            print("True 9")
            if self.logic_list[8] != False:
                print("no")
                return self.now_clik
            else:
                DrawNew.DrawNewElement(self)
                return not self.now_clik
        else:
            print("Is not play ground")
            return self.now_clik

class DrawNew:
    def DrawNewElement(self):
        if self.now_clik == False:
            buf = Such.Sucher(self)
            self.logic_list[buf] = 1
            print("False")
        elif self.now_clik == True:
            buf = Such.Sucher(self)
            self.logic_list[buf] = 2
            print("True")
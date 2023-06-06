import pygame

class Button(object):
        def __init__(self, name, x, y, width, height, color, display = ""):
                self.name = name
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.color = color
                self.rec = pygame.Rect(self.x, self.y, self.width, self.height)
                self.display = display
        def draw(self, win):
                self.rec = pygame.Rect(self.x, self.y, self.width, self.height)
                pygame.draw.rect(win, self.color, self.rec, 0)
                font = pygame.font.SysFont('arial', 30, True)
                text = font.render(self.display, 1, (0,0,0))
                win.blit(text, ((self.x + self.width / 2) - 6 * len(self.display), (self.y + self.height / 2) - 17))
import pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)

class Grid():
    def __init__(self):
        self.pixels = [[0 for _ in range(28)] for _ in range(28)]

    def draw(self, window):
        window.fill(white)
        pixel_size = window.get_width() // 28
        for i in range(28):
            for j in range(28):
                if self.pixels[i][j] == 1:
                    x = i * pixel_size
                    y = j * pixel_size
                    pygame.draw.rect(window, black, (x, y, pixel_size, pixel_size))
    def update(self, mouse, window_size):
        x = mouse[0] // 20
        y = mouse[1] // 20
        self.pixels[x][y] = 1

def main():

    grid = Grid()
    size = 560
    window = pygame.display.set_mode((size,size))
    running = 1
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    pass
                elif pygame.mouse.get_pressed()[0] == True:
                    grid.update(pygame.mouse.get_pos(), size)
        grid.draw(window)
        pygame.display.update()
if __name__ == '__main__':
    pygame.init()
    main()

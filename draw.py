import pygame
from pygame.locals import *
from train import Model
import numpy as np
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
        x = mouse[0] // (window_size // 28)
        y = mouse[1] // (window_size // 28)
        for i in range(-1, 2):
            if i+x >= 28 or i+x < 0:
                continue
            for j in range(-1, 2):
                if j+y >= 28 or j+y < 0:
                    continue
                self.pixels[i+x][y+j] = 1

def main():

    grid = Grid()
    model = Model()
    size = 560
    window = pygame.display.set_mode((size,size))
    running = 1
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    im = np.array(grid.pixels).T.tolist()
                    predict = model.predict(im)
                    print(predict)
                    grid = Grid()
                elif pygame.mouse.get_pressed()[0] == True:
                    grid.update(pygame.mouse.get_pos(), size)
        grid.draw(window)
        pygame.display.update()
    if not model.is_saved():
        model.save()
if __name__ == '__main__':
    pygame.init()
    main()

import pygame
from pygame.locals import *
from train import Model
import numpy as np
from tkinter import *
import tkinter.messagebox as msg
white = (255,255,255)
black = (0,0,0)
gray1 = (128,128,128)
gray2 = (192,192,192)

class Grid():
    def __init__(self):
        self.pixels = [[0 for _ in range(28)] for _ in range(28)]

    def draw(self, window):
        window.fill(white)
        pixel_size = window.get_width() // 28
        for i in range(28):
            for j in range(28):
                if self.pixels[i][j] == 0:
                    continue
                x = i * pixel_size
                y = j * pixel_size
                color = None
                rect = (x, y, pixel_size, pixel_size)
                if self.pixels[i][j] == 1:
                    color = black
                elif self.pixels[i][j] == 0.5:
                    color = gray1
                elif self.pixels[i][j] == 0.25:
                    color = gray2
                pygame.draw.rect(window, color, rect)
    def update(self, mouse, window_size):
        x = mouse[0] // (window_size // 28)
        y = mouse[1] // (window_size // 28)
        self.pixels[x][y] = 1
        self.update_diag(x, y)
        self.update_orth(x, y)
    def in_range(x, y):
        return x < 28 and y < 28 and x >= 0 and y >=0
    def update_diag(self, x, y):
        for i in range(x-1, x+2, 2):
            for j in range(y-1, y+2, 2):
                if Grid.in_range(i, j) and self.pixels[i][j] < 0.25:
                    self.pixels[i][j] = 0.25
    def update_orth(self, x, y):
        for i in range(-1, 2, 2):
            if Grid.in_range(x+i, y) and self.pixels[x+i][y] < 0.5:
                self.pixels[x+i][y] = 0.5
            if Grid.in_range(x, y+i) and self.pixels[x][y+i] < 0.5:
                self.pixels[x][y+i] = 0.5
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
                    popup = Tk()
                    popup.withdraw()
                    msg.showinfo("Prediction", "The model predicted this number is a " + str(predict))
                    popup.destroy()
                    grid = Grid()
                elif pygame.mouse.get_pressed()[0] == True:
                    grid.update(pygame.mouse.get_pos(), size)
        grid.draw(window)
        pygame.display.update()
if __name__ == '__main__':
    pygame.init()
    main()

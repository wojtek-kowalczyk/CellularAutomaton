import time
import pygame
from random import randrange

# settings
ROWS = 40
COLS = 40
PPU = 16  # px per unit
PRIMARY_COLOR = (255, 255, 255)
SECONDART_COLOR = (0, 0, 0)
BORDER = 1
CA_NEIGHBORS = 4
ITERATIONS = 1
DELAY = 1


def CA(grid):
    newGrid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            newGrid[i][j] = seeNeighbors(grid, i, j)
    return newGrid


def seeNeighbors(grid, row, col):
    countOnes = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            try:
                if grid[row+i][col+j] == 1:
                    countOnes += 1
            except:
                print("BORDER: " + str(row) + ", " + str(col))
                return BORDER
    if countOnes >= CA_NEIGHBORS:
        return 1
    else:
        return 0


def generateGrid():
    return [[randrange(2) for i in range(COLS)] for j in range(ROWS)]


def drawGrid(grid, screen):
    for i in range(ROWS):
        for j in range(COLS):
            color = PRIMARY_COLOR if grid[i][j] == 0 else SECONDART_COLOR
            pygame.draw.rect(screen, color,
                             pygame.Rect(j*PPU, i*PPU, PPU, PPU))
    pygame.display.flip()


def printGrid(grid):
    for i in range(ROWS):
        for j in range(COLS):
            print(str(grid[i][j])+", ", end='')
        print()


if __name__ == "__main__":

    screen = pygame.display.set_mode((COLS*PPU, ROWS*PPU))
    screen.fill((150, 150, 150))
    pygame.display.set_caption("Cellular Automaton")
    grid = generateGrid()
    drawGrid(grid, screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print("running iteration")
                grid = CA(grid)
                drawGrid(grid, screen)
                time.sleep(0.5)

import time
import pygame
from random import randrange

# settings
ROWS = 50
COLS = 50
PPU = 8  # px per unit
PRIMARY_COLOR = (255, 255, 255)  # 1 on grid - WHITE
SECONDART_COLOR = (0, 0, 0)  # 0 on grid - BLACK
ITERATIONS = 1
DELAY = 1
WHITE = 1
BLACK = 0

CA_NEIGHBORS = 4  # set this to 4 for "become majority" behaviour
PERCENT_FILL = 50  # 0-100
FILL_WITH = WHITE  # intedned behaviour only for BLACK and WHITE (0 and 1)
BORDER = WHITE  # BLACK -> gives caves | WHITE -> gives islands
TILING = True  # if True -> BORDER has no effect

# modify this to achieve different result.


def rule(neighboringOnes, centerValue):
    """
    This function returns what the current cell must become dependant on it's neighbors
    """
    # neighboringZeros = 8 - neighboringOnes
    if neighboringOnes > CA_NEIGHBORS:
        return WHITE
    elif neighboringOnes == CA_NEIGHBORS:
        return centerValue
    else:
        return BLACK


def CA(grid):
    newGrid = [row[:] for row in grid]
    for i in range(ROWS):
        for j in range(COLS):
            newGrid[i][j] = seeNeighbors(grid, i, j)
    return newGrid


def seeNeighbors(grid, row, col):
    countWhites = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            if TILING:
                if grid[(row+i) % ROWS][(col+j) % COLS] == WHITE:
                    countWhites += 1
            else:
                if row+i < 0 or row+i >= ROWS or col+j < 0 or col+j >= COLS:
                    return BORDER
                if grid[row+i][col+j] == WHITE:
                    countWhites += 1
    return rule(countWhites, grid[row][col])


def generateGrid():
    return [[FILL_WITH if PERCENT_FILL > randrange(100) else abs(FILL_WITH-1) for i in range(COLS)] for j in range(ROWS)]


def drawGrid(grid, screen):
    for i in range(ROWS):
        for j in range(COLS):
            color = PRIMARY_COLOR if grid[i][j] == WHITE else SECONDART_COLOR
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
                grid = CA(grid)
                drawGrid(grid, screen)

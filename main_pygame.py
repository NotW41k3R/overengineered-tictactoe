import pygame
from gamesprites import Cell
from board import Board
from player import Player
from bot import Bot

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()
running = True

BOARD_SIZE = 480
CELL_SIZE = BOARD_SIZE // 3
OFFSET = (WIDTH - BOARD_SIZE) // 2

BG_COLOR = (25, 35, 45)
BOARD_COLOR = (40, 55, 70)
GRID_COLOR = (220, 220, 220)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    board_rect = pygame.Rect(OFFSET, OFFSET, BOARD_SIZE, BOARD_SIZE)
    pygame.draw.rect(screen, BOARD_COLOR, board_rect, border_radius=12)

    for i in range(1, 3):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (OFFSET + i * CELL_SIZE, OFFSET),
            (OFFSET + i * CELL_SIZE, OFFSET + BOARD_SIZE),
            8
        )

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (OFFSET, OFFSET + i * CELL_SIZE),
            (OFFSET + BOARD_SIZE, OFFSET + i * CELL_SIZE),
            8
        )

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        if (
            OFFSET <= mouse_x <= OFFSET + BOARD_SIZE and
            OFFSET <= mouse_y <= OFFSET + BOARD_SIZE
        ):
            board_x = mouse_x - OFFSET
            board_y = mouse_y - OFFSET

            col = board_x // CELL_SIZE
            row = board_y // CELL_SIZE

            print("Clicked cell:", row, col)


    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
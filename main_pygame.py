import pygame
from board import Board
from player import Player
from bot import Bot

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()
font_title = pygame.font.SysFont(None, 72)
font_button = pygame.font.SysFont(None, 48)

running = True
state_change_time = 0
STATE_COOLDOWN = 300  

BOARD_SIZE = 480
CELL_SIZE = BOARD_SIZE // 3
OFFSET = (WIDTH - BOARD_SIZE) // 2

BG_COLOR = (25, 35, 45)
BOARD_COLOR = (40, 55, 70)
GRID_COLOR = (220, 220, 220)

GAME_STATES = ["MENU_MODE_SELECT", "MENU_SYMBOL_SELECT", "PLAYING", "GAME_OVER"]
CURRENT_STATE = GAME_STATES[0]

friend_button = pygame.Rect(WIDTH//2 - 110, HEIGHT//2 - 40, 220, 60)
bot_button = pygame.Rect(WIDTH//2 - 110, HEIGHT//2 + 40, 220, 60)

x = pygame.image.load('art/x.png').convert_alpha()
o = pygame.image.load('art/o.png').convert_alpha()
x_selection_button = x.get_rect(center=(WIDTH//2 - 100, HEIGHT//2))
o_selection_button = o.get_rect(center=(WIDTH//2 + 100, HEIGHT//2))

GAME_SYMBOLS = [x,o]

board = Board()
player1 = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    if CURRENT_STATE == "MENU_MODE_SELECT":

        title_surface = font_title.render("Select Mode", True, (230, 230, 230))
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        pygame.draw.rect(screen, (70, 130, 180), friend_button, border_radius=12)
        pygame.draw.rect(screen, (70, 130, 180), bot_button, border_radius=12)

        friend_text = font_button.render("Friend", True, (20, 20, 20))
        bot_text = font_button.render("Bot", True, (20, 20, 20))

        screen.blit(friend_text, friend_text.get_rect(center=friend_button.center))
        screen.blit(bot_text, bot_text.get_rect(center=bot_button.center))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if friend_button.collidepoint(event.pos):
                print("Friend selected")
                player2 = Player()
                CURRENT_STATE = GAME_STATES[1]
                state_change_time = pygame.time.get_ticks()

            if bot_button.collidepoint(event.pos):
                print("Bot selected")
                player2 = Bot()
                CURRENT_STATE = GAME_STATES[1]
                state_change_time = pygame.time.get_ticks()
        
    if CURRENT_STATE == "MENU_SYMBOL_SELECT":
        title_surface = font_title.render("Select X or O", True, (230, 230, 230))
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        screen.blit(x, x_selection_button)
        screen.blit(o, o_selection_button)

        current_time = pygame.time.get_ticks()
        turn=False
        if current_time - state_change_time >= STATE_COOLDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x_selection_button.collidepoint(event.pos):
                    print("X selected")
                    player1.player_number = 1
                    player2.player_number = -1
                    player_list = [player1,player2]
                    CURRENT_STATE = GAME_STATES[2]
                    state_change_time = pygame.time.get_ticks()

                if o_selection_button.collidepoint(event.pos):
                    print("O selected")
                    player1.player_number = -1
                    player2.player_number = 1
                    player_list = [player2, player1]
                    CURRENT_STATE = GAME_STATES[2]
                    state_change_time = pygame.time.get_ticks()

    if CURRENT_STATE == "PLAYING":

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

        for row in range(3):
            for col in range(3):
                value = board.state[row][col]
                if not value:
                    continue
                else:
                    if value == 1: value=0
                    cell_x = OFFSET + col * CELL_SIZE
                    cell_y = OFFSET + row * CELL_SIZE
                    center_x = cell_x + CELL_SIZE // 2
                    center_y = cell_y + CELL_SIZE // 2

                    screen.blit(GAME_SYMBOLS[value], GAME_SYMBOLS[value].get_rect(center=(center_x, center_y)))
                
        current_time = pygame.time.get_ticks()
        if isinstance(player_list[turn], Player):
            if current_time - state_change_time >= STATE_COOLDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    if (OFFSET <= mouse_x <= OFFSET + BOARD_SIZE and OFFSET <= mouse_y <= OFFSET + BOARD_SIZE):
                        board_x = mouse_x - OFFSET
                        board_y = mouse_y - OFFSET

                        col = board_x // CELL_SIZE
                        row = board_y // CELL_SIZE

                        if board.is_move_valid((row,col)):
                            board.apply_move((row,col), player_list[turn])

                            cell_x = OFFSET + col * CELL_SIZE
                            cell_y = OFFSET + row * CELL_SIZE
                            center_x = cell_x + CELL_SIZE // 2
                            center_y = cell_y + CELL_SIZE // 2

                            screen.blit(GAME_SYMBOLS[turn], GAME_SYMBOLS[turn].get_rect(center=(center_x, center_y)))

                            turn = not turn
                            board.print_board()

                            if board.check_win():
                                winner = turn
                                CURRENT_STATE = GAME_STATES[3]

                            if board.check_draw():
                                winner = None
                                CURRENT_STATE = GAME_STATES[3]
        else:
            current_time = pygame.time.get_ticks()
            if current_time - state_change_time >= STATE_COOLDOWN:
                move = player2.get_move(board)

                if board.is_move_valid(move):
                    board.apply_move(move, player_list[turn])

                    cell_x = OFFSET + move[1] * CELL_SIZE
                    cell_y = OFFSET + move[0] * CELL_SIZE
                    center_x = cell_x + CELL_SIZE // 2
                    center_y = cell_y + CELL_SIZE // 2

                    screen.blit(GAME_SYMBOLS[turn], GAME_SYMBOLS[turn].get_rect(center=(center_x, center_y)))

                    turn = not turn
                    board.print_board()

                    if board.check_win():
                        winner = turn
                        CURRENT_STATE = GAME_STATES[3]

                    if board.check_draw():
                        winner = None
                        CURRENT_STATE = GAME_STATES[3]
                        
    if CURRENT_STATE == "GAME_OVER":
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

        for row in range(3):
            for col in range(3):
                value = board.state[row][col]
                if not value:
                    continue
                else:
                    if value == 1: value=0
                    cell_x = OFFSET + col * CELL_SIZE
                    cell_y = OFFSET + row * CELL_SIZE
                    center_x = cell_x + CELL_SIZE // 2
                    center_y = cell_y + CELL_SIZE // 2

                    screen.blit(GAME_SYMBOLS[value], GAME_SYMBOLS[value].get_rect(center=(center_x, center_y)))
        
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        if winner is None:
            result_text = "It's a Draw!"
        elif winner == 1:
            result_text = "X Wins!"
        else:
            result_text = "O Wins!"

        result_surface = font_title.render(result_text, True, (255, 255, 255))
        result_rect = result_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(result_surface, result_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
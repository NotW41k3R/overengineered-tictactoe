import numpy as np
from board import Board
from player import Player
from parser import Parser

PLAYERS = ['X', 'O']
POSSIBLE_LEVELS = ['a','b','c']
POSSIBLE_BLOCKS = ['1','2','3']
LEVEL_NUM = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
}
VALUE_MAP = {
    1: 'X',
    -1: 'O',
    0: '_',
}

# Ask player to play a move
def play_move(player):
    position = input(f"{VALUE_MAP[player.player_number]}'s turn: ").lower()
    move = parser.parse_move(position)
    return move

# Initialise Board
board = Board()
board.print_board()

# Initialise Players
player1 = Player()
player2 = Player()

parser = Parser()

# CHOOOSE X OR O
player1_symbol = input("Choose X or O: ").upper()
if player1_symbol not in PLAYERS:
    print("Please pick X or O")
else:
    if player1_symbol == 'X':
        player1.player_number = 1
        player2.player_number = -1
        player_list = [player1,player2]
    else:
        player1.player_number = -1
        player2.player_number = 1
        player_list = [player2, player1]
    i=False
    # Game Loop
    game_is_on = True
    while game_is_on:
        current_player = player_list[i]
        move = play_move(current_player)

        while not move:
            print("Please enter a valid move.")
            move = play_move(current_player)

        while not board.is_move_valid(move):
            print("Please enter a valid move.")
            move = play_move(current_player)
            
        board.apply_move(move,current_player)
        board.print_board()
        if board.check_win():
            print(f"{VALUE_MAP[current_player.player_number]} has won")
            game_is_on = False

        if board.check_draw():
            print("Its a Draw")
            game_is_on = False
        i = not i
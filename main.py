from board import Board
from player import Player
from bot import Bot

PLAYER_CHOICE = ['F', 'B']
PLAYERS = ['X', 'O']
VALUE_MAP = {
    1: 'X',
    -1: 'O',
    0: '_',
}

# Ask player to play a move
def play_move(player, board):
    if isinstance(player, Player):
        return player.get_move()
    elif isinstance(player, Bot):
        print(f"{VALUE_MAP[player.player_number]}'s turn")
        return player.get_move(board)

# Initialise Board
board = Board()
board.print_board()

# Initialise Players
player1 = Player()
player_choice = input("Do want to play against a friend or bot? write F or B: ").upper()
if player_choice not in PLAYER_CHOICE:
    print("Please pick Friend (F) or Bot(B)")
else: 
    if player_choice == "F":
        player2 = Player()
    else: 
        player2 = Bot()

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
            move = play_move(current_player, board)

            if isinstance(current_player, Player):
                while not move:
                    print("Please enter a valid move.")
                    move = play_move(current_player, board)

                while not board.is_move_valid(move):
                    print("Please enter a valid move.")
                    move = play_move(current_player, board)
                
            board.apply_move(move,current_player)
            board.print_board()
            if board.check_win():
                print(f"{VALUE_MAP[current_player.player_number]} has won")
                game_is_on = False

            if board.check_draw():
                print("Its a Draw")
                game_is_on = False
            i = not i
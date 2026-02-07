PLAYERS = ['X', 'O']
POSSIBLE_LEVELS = ['a','b','c']
POSSIBLE_BLOCKS = ['1','2','3']
LEVEL_NUM = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
}

# Print the Board
def print_board(state):
    print("      1   2   3")
    print("    +---+---+---+")
    
    row_labels = ['a', 'b', 'c']
    
    for i, row in enumerate(state):
        row_display = f"{row_labels[i]} | {row[0]} | {row[1]} | {row[2]} |"
        print(f"  {row_display}")
        print("    +---+---+---+")



# Initialise a New Board
def initialise_board():
    a = ["_","_","_"]
    b = ["_","_","_"]
    c = ["_","_","_"]
    state = [a,b,c]
    print_board(state)
    return state


# Place a marker on the board
def place_marker(marker, move, current_state):
    current_state[LEVEL_NUM[move[0]]][int(move[1])-1] = marker
    return current_state


# Ask player to play a move
def play_move(player):
    position = input(f"{player}'s turn: ")
    if len(position)==2:
        move = parse_move(position)
        return move
    else:
        print("Please Enter a 2 character coordinate, for example 'a1'")
        move = play_move(player)
        return move


# Parse the User inputted move
def parse_move(position):
    # PARSE ALPHABET
    level = position[0]

    # PARSE NUMERIC
    block = position[1]
    
    move = [level,block]

    return move


# Check if a move is valid AND the cell is vacant
def is_move_valid(current_state, move):
    if move[0].isalpha() and move[0] in POSSIBLE_LEVELS and move[1] in POSSIBLE_BLOCKS:
        if current_state[LEVEL_NUM[move[0]]][int(move[1])-1] == "_":
            return True
        else:
            return False
    else:
        return False


# Check Win
def check_win(state):
    # Horizontal Win
    for level in state:
        if level[0] != "_" and level[0] == level[1] == level[2]:
            return True
    
    # Vertical Win
    for i in range(3):
        if state[0][i] != "_" and state[0][i] == state[1][i] == state[2][i]:
            return True
    
    # Diagonal Win
    if state[0][0] != "_" and state[0][0] == state[1][1] == state[2][2]:
        return True 
    if state[1][1] != "_" and state[2][0] == state[1][1] == state[0][2]:
        return True 
    return False


# Draw
def check_draw(state):
    return all("_" not in row for row in state)

        
# INITIALISE BOARD
game_is_on = True
state = initialise_board()

# CHOOOSE X OR O
player1 = input("Choose X or O: ").upper()
if player1 not in PLAYERS:
    print("Please pick X or O")
else:
    if player1 == 'X':
        player2 = 'O'
    else:
        player2='X'

    player_list = [player1, player2]
    i = False

    while game_is_on:
        valid_move = False
        player = player_list[i]

        while not valid_move:
            move = play_move(player)
            if is_move_valid(state,move):
                valid_move = True
            else:
                print("Either the Cell is taken or the move is invalid")
                valid_move = False

        state = place_marker(player, move, state)
        print_board(state)

        if check_win(state):
            print(f"{player} has won")
            game_is_on = False
        if check_draw(state):
            print("Its a Draw")
            game_is_on = False

        i = not i 
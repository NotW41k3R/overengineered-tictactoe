import numpy as np
SYMBOL_MAP={
    0 : '_',
    1 : 'X',
    -1 : 'O'
}

class Board:
    def __init__(self):
        self.state = np.array([[0,0,0],[0,0,0],[0,0,0]])

    def reset_board(self):
        self.state = np.array([[0,0,0],[0,0,0],[0,0,0]])

    def print_board(self):
        print("   +---+---+---+")
        for i in range(3):
            row_display = f" | {SYMBOL_MAP[self.state[i][0]]} | {SYMBOL_MAP[self.state[i][1]]} | {SYMBOL_MAP[self.state[i][2]]} |"
            print(f"  {row_display}")
            print("   +---+---+---+")

    def is_move_valid(self, move):
        if self.state[move] == 0:
            return True
        return False

    def apply_move(self, move, player):
        self.state[move] = player.player_number

    def check_win(self):
        row_sums = abs(self.state.sum(axis=1))
        column_sum = abs(self.state.sum(axis=0))
        diag1 = abs(np.trace(self.state))
        diag2 = abs(np.trace(np.fliplr(self.state)))

        if 3 in row_sums or 3 in column_sum or diag1==3 or diag2==3:
            return True
        
        return False
        
    def check_draw(self):
        return not np.any(self.state == 0)


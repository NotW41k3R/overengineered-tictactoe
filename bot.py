import numpy as np

PLAYERS = ['X', 'O']
SYMBOL_MAP={
    'X':1,
    'O':-1,
}
VALUE_MAP = {
    1: 'X',
    -1: 'O',
    0: '_',
}

class Bot:
    def __init__(self):
        self.player_number = 0

    def get_move(self, board):
        empty_spots = np.argwhere(board.state == 0)
        if np.any(np.all(empty_spots == [1,1], axis=1)):
            return (1,1)
        else:
            row_sums = board.state.sum(axis=1)
            column_sum = board.state.sum(axis=0)
            diag1 = np.trace(board.state)
            diag2 = np.trace(np.fliplr(board.state))

            if 2 in row_sums:
                row_indices = np.argwhere(row_sums==(self.player_number*-2))
                row = board.state[row_indices[0,0]]
                column = np.argwhere(row == [0])
                move = (row_indices[0,0], column[0,0])
                return move
                
            if 2 in column_sum:
                column_indices = np.argwhere(column_sum==(self.player_number*-2))
                column = board.state[:, column_indices[0,0]]
                row = np.argwhere(column == [0])
                move = (row[0,0], column_indices[0,0])
                return move
            
            if diag1 == self.player_number*-2:
                diag = np.diag(np.fliplr(board.state))
                diag_idx = np.argwhere(diag == 0)
                if diag_idx.size > 0:
                    i = diag_idx[0, 0]
                    rows, cols = np.diag_indices(3)
                    move = (rows[i], cols[i])
                    return move


            if diag2 == self.player_number*-2:
                diag = np.diag(np.fliplr(board.state))
                diag_idx = np.argwhere(diag == 0)
                if diag_idx.size > 0:
                    i = diag_idx[0, 0]
                    rows, cols = np.diag_indices(3)
                    cols = cols[::-1]
                    move = (rows[i], cols[i])
                    return move

            
        move = (empty_spots[0][0], empty_spots[0][1])
        return move
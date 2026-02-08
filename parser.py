LEVEL_NUM = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
}
POSSIBLE_LEVELS = ['a','b','c']
POSSIBLE_BLOCKS = ['1','2','3']

class Parser:
    def __init__(self):
        pass

    def parse_move(self, move):
        if len(move)==2:
            if move[0].isalpha() and move[0] in POSSIBLE_LEVELS and move[1] in POSSIBLE_BLOCKS:
                level = LEVEL_NUM[move[0]]
                block = int(move[1]) - 1
                move = (level,block)
                return move
            else:
                return None
        else:
            return None
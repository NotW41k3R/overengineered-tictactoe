from parser import Parser
parser = Parser()
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
class Player:
    def __init__(self):
        self.player_number = 0

    def get_move(self):
        position = input(f"{VALUE_MAP[self.player_number]}'s turn: ").lower()
        if position=='exit':
            return exit
        move = parser.parse_move(position)
        return move
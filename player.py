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
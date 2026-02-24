import numpy as np
import random
import json
from board import Board

PLAYERS = [1, -1]

class RLAgent:

    def __init__(self):
        self.move_history = []
        self.path = "qtable.json"
        self.learning_rate = 0.1
        self.epsilon = 0.01
        self.load_q_table(self.path)
        self.player_number = 0

    def encode_state(self, board):
        flat = board.state.flatten()

        return ",".join(str(x) for x in flat)
    
    def choose_action(self, board):
        key = self.encode_state(board)

        if key not in self.q_table:
            self.q_table[key] = [0] * 9
        
        valid_moves = board.get_valid_moves()
        moves = self.encode_moves(valid_moves)
        number = random.random()

        if number < self.epsilon:
            move = random.choice(valid_moves)
            index = move[0]*3 + move[1]
            self.move_history.append((key, index, self.player_number))
            return move
        else:
            q_state = self.q_table[key]
            possible_moves = []
            for move in moves:
                possible_moves.append(q_state[move])

            best_move_score = max(possible_moves)
            best_move_index = possible_moves.index(best_move_score)
            move = valid_moves[best_move_index]
            index = move[0]*3 + move[1]
            self.move_history.append((key, index, self.player_number))
            return move

                
    def encode_moves(self,valid_moves):
        moves = [ r*3+c for (r,c) in valid_moves]
        return moves
    
    def learn(self, reward, winner):

        for (state_key, action_index, player) in self.move_history:
            if player != winner:
                continue
            q_values = self.q_table[state_key]
            old_value = q_values[action_index]

            difference = reward - old_value
            adjustment = self.learning_rate * difference

            new_value = old_value + adjustment

            q_values[action_index] = new_value

        self.move_history = []

    def save_q_table(self, path):
        with open(path, "w") as f:
            json.dump(self.q_table, f)

    def load_q_table(self, path):
        try:
            with open(path, "r") as f:
                self.q_table = json.load(f)
        except FileNotFoundError:
            self.q_table = {}

    def train_self_play(self,num):
        board = Board()
        for _ in range(num):
            board.reset_board()
            self.move_history = []
            i = False
            game_is_on = True
            while game_is_on:
                self.player_number = PLAYERS[i]
                
                move = self.choose_action(board)
                board.apply_move(move, self)

                if board.check_win():
                    winner_player = self.player_number
                    self.learn(1, winner_player)
                    break

                if board.check_draw():
                    self.learn(0, 0)
                    break
                i = not i

# agent = RLAgent()
# agent.train_self_play(200000)
# agent.save_q_table("qtable.json")
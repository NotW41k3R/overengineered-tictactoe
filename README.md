# Overengineered CLI-Based TicTacToe

This is the most overengineered version of TicTacToe i could think of, goal was to make a simple game of tictactoe, but now this version has...

## Features

* **Bot Player**
  A Defensive bot that defends threats across rows, columns and diagonals, it blocks all winning moves using vectorized evaluation.(Defense so good you might lose to it).

* **Object-Oriented Structure**
  Clean separation into `Board`, `Player`, and `Parser` classes.

* **NumPy Board Representation**
  Fast ndarray-based 3×3 game state with vectorized operations.

* **Input Parser**
  Converts moves like `a2` into numeric coordinates.

* **Move Validator**
  Ensures moves are in bounds and placed on empty cells.

* **Win/Draw Logic**
  Uses NumPy row/column/diagonal sums for instant state evaluation.

* **Game Loop**
  Controls turn order, retries invalid actions, and runs the match flow.

* **Board Renderer**
  Prints a clear, readable representation of the current game board.

---
## How to Run

1. Make sure you have **Python 3+** installed.
2. Install the required packages:

```bash
pip install -r requirements.txt
python main.py
```

---

## Future Improvements (TODO)

* ~~Maybe rewrite using OOP for fun~~
* ~~Convert the board from a nested list to a numpy array~~
* ~~Add a bot opponent~~
* Maybe Train a ML agent to act as the game’s opponent.
* Add a difficulty selector
* Implement a “self-play” mode (bot vs bot for training)
* Add a replay mode (watch a stored match move-by-move)


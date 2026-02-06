# Overengineered CLI-Based TicTacToe

This is the most overengineered version of TicTacToe i could think of, goal was to make a simple game of tictactoe, but now this version has...

## Features

* **Game State Controller**
  Handles whose turn it is.

* **Game Loop**
  Keeps everything runnign and can handle retries if a move is invalid.

* **Input Parser**
  Interprets user input like `a2` into board coordinates.

* **Move Validator**
  Checks bounds and vacancy so no one can break the game.

* **Board Logic**
  Stores the board state and prints the board in the terminal.

All that in a single main.py

---

## How to Run

Requires **Python 3+**.

```bash
python main.py
```

---

## Future Improvements (TODO)

* Add win detection
* Add draw detection
* Add colored CLI output
* Add a bot opponent
* Maybe rewrite using OOP for fun

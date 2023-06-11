## Jankenpon Game - *Rock, Paper, Scissors Game*

This is a simple Rock, Paper, Scissors game implemented in Python. The player plays against the computer and the objective is to win as many rounds as possible.

## How to play

The implemented game works as follows: scissors cut paper, but break with stone; the paper wraps around the rock but is cut by the scissors and the rock breaks the scissors and is wrapped by the paper.

If the player chooses paper in the terminal and the machine chooses stone, the player earns a point, if the player chooses stone and the machine chooses paper, the machine earns a point.

The player can continue the game through the input by selecting the option **Y** for Yes and **N** for No.

## Prerequisites

It requires no prerequisites, you only need to run the script. If you don't have Python installed, you can visit [here](https://www.python.org/downloads/) to download Python

## How to run the script

Running the script is pretty easy, open a terminal in the folder where your script is located and run the following command :

python3 run.py

## Commands to Play

- shell
- Copy code
- python3 run.py
- Follow the instructions displayed on the terminal to select your move (Rock, Paper, Scissors).

- The computer will also make its move.

- The result of each round will be displayed on the terminal.

- The game will continue until you choose to end it.

## Sample use of the script

![run.python Screenshot](https://github.com/jmartinesdev/jankenpon-game/blob/main/images/jankenpon-game.png)

## User Stories

1. As a user, I want to view the current state of the board and my opponent's board.
2. As a user, I want to make valid guesses and receive feedback on hits and misses.
3. As a user, I want to track my score and my opponent's score during gameplay.
4. As a user, I want to have the option to play again after the game ends.

## Scope

* The game should provide an interactive interface for players to enter their guesses.
* The game should validate user input and provide appropriate feedback.
* The game should track the scores of both the player and the computer.
* The game should have a clear termination condition and offer the option to play again.

## Testing 

The Jankenpon Game has been tested extensively to ensure its functionality and accuracy. The code was passed through [PEP8](https://pep8ci.herokuapp.com/#) Python Validator and no issues were found. The line lengths have been adjusted to adhere to the recommended maximum of 79 characters per line.



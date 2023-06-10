from random import choice

cpu_victory = 0
player_victory = 0


def player_mov():
    """
    Here the player's choices between rock, paper and scissors will be defined.
    """
    player_choice = input("Choose one: Rock, Paper or Scissors: ")
    if player_choice in ['ROCK', 'Rock', 'rock']:
        player_choice = 'pedra'
    elif player_choice in ['PAPER', 'Paper', 'paper']:
        player_choice = 'paper'
    elif player_choice in ['SCISSOR', 'Scissor', 'scissor']:
        player_choice = 'scissor'
    else:
        print('Invalid! Please choose rock, paper or scissor. Tente novamente')
        player_mov()
    return player_choice

def cpu_mov():
    """""
    The machine choice an option to player
    """""
    cpu_choice = choice(['rock', 'paper', 'scissor'])
    return cpu_choice
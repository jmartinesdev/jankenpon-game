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
        print('Invalid! Please choose rock, paper or scissor. Try again!')
        player_mov()
    return player_choice


def cpu_mov():

    """""
    The machine choice an option to player
    """""

    cpu_choice = choice(['rock', 'paper', 'scissor'])
    return cpu_choice


while True:

    """
    Added looping structure. The game will repeat as
    long as the player wants to play.
    """

    print('---------')

    cpu_choice = cpu_mov()
    player_choice = player_mov()

    print('---------')

    """
    structure if add to the player win
    """

    if (player_choice == 'rock' and cpu_choice == 'scissor') or \
        (player_choice == 'scissor' and cpu_choice == 'paper') or \
            (player_choice == 'paper' and cpu_choice == 'rock'):
        print(f'Player choose {player_choice} and the machine choose'
              f'{cpu_choice}.' 'Result: You lost!')
        player_victory += 1

    elif player_choice == cpu_choice:
        print(f'Player choose {player_choice} and the machine choose'
              f'{cpu_choice}.' 'Result: Players draw!')

    else:
        print(f'Player choose {player_choice} and the machine choose'
              f'{cpu_choice}.' 'Result: You lost!')
        cpu_victory += 1

    print('----------')

    """
    Add a print to show the player
    on the screen the number of wins
    """

    print(f"Total players victories: {player_victory}")
    print(f"Total machine victories: {cpu_victory}")

    print('-----------')

    player_choice = input('Do you want play again? (y/n)')

    """
    Here we are going to check the while structure for
    the player to choose whether to continue playing or not.
    """

    if player_choice in ['yes', 'YES', 'Yes', 'y', 'Y']:
        pass
    elif player_choice in ['NO', 'no', 'No', 'n', 'N']:
        break
    else:
        break

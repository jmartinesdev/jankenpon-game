from random import choice

cpu_victory = 0
player_victory = 0


def player_mov():
    """
    Here the player's choices between rock, paper and scissors will be defined.
    """
    player_choice = input("Choose one: Rock, Paper or Scissors: ").lower()
    if player_choice not in ['rock', 'paper', 'scissor']:
        print('Invalid! Please choose rock, paper or scissors. Try again!!')
        return player_mov()
    return player_choice

def cpu_mov():
    cpu_choice = choice(['rock', 'paper', 'scissors'])
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

    if (player_choice == 'rock' and cpu_choice == 'scissors') or \
        (player_choice == 'scissors' and cpu_choice == 'paper') or \
            (player_choice == 'paper' and cpu_choice == 'rock'):
        print(f'Player chooses {player_choice} and the machine chooses {cpu_choice}. Result: You win!')
        player_victory += 1

    elif player_choice == cpu_choice:
        print(f'Player chooses {player_choice} and the machine chooses {cpu_choice}. Result: Draw!')

    else:
        print(f'Player chooses {player_choice} and the machine chooses {cpu_choice}. Result: You lose!')
        cpu_victory += 1

    print('----------')

    """
    Add a print to show the player
    on the screen the number of wins
    """

    print(f"Total players victories: {player_victory}")
    print(f"Total machine victories: {cpu_victory}")
    print('-----------')
    
    """
    Here we are going to check the while structure for
    the player to choose whether to continue playing or not.
    """

    replay_choice = input('Do you want to play again? (y/n): ').lower()
    if replay_choice not in ['y', 'yes']:
        break

###############################################################################
# Description: Rock, paper, and scissor game against the computer with random choices
###############################################################################
import random

# get computer's choice
def get_computer_choice():
    random_choice = random.randint(1,3)
    if random_choice == 1:
        return 'rock'
    elif random_choice == 2:
        return 'paper'
    else:
        return 'scissors'

# get player's choice
def get_player_choice():
    choice = input('Choose rock, paper, or scissors: ')
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        print('You made an invalid choice. Please try again.')
        choice = input('Choose rock, paper, or scissors: ')

    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return choice

def main():
    # Write your mainline logic here ------------------------------------------
    user_choice = get_player_choice()
    comp_choice = get_computer_choice()
    print(f'  The computer chose {comp_choice}, and you chose {user_choice}.')
    winner = get_winner(comp_choice, user_choice)
    while winner == 'tie':
        print('  Its a tie. Starting over.')
        print('')
        user_choice = get_player_choice()
        comp_choice = get_computer_choice()
        print(f'  The computer chose {comp_choice}, and you chose {user_choice}.')
        winner = get_winner(comp_choice, user_choice)
        break

    if winner == 'computer':
        print(f'  {comp_choice} beats {user_choice}')
        print('  You lost.  Better luck next time.')
    elif winner == 'player':
        print(f'  {user_choice} beats {comp_choice}')
        print('  You won the game!')

    print('Thanks for playing.')


# get winner function
def get_winner(comp_choice, user_choice):
    #paper_message = '  paper beats rock'
    #rock_message = '  rock beats scissors'
    #scissors_message = '  scissors beats paper'
    winner = ''

    if comp_choice == user_choice:
        winner = 'tie'

    elif comp_choice == 'rock' and user_choice == 'scissors':
        #print(rock_message)
        winner = 'computer'

    elif comp_choice == 'scissors' and user_choice == 'rock':
        #print(rock_message)
        winner = 'player'

    elif comp_choice == 'scissors' and user_choice == 'paper':
        #print(scissors_message)
        winner = 'computer'

    elif comp_choice == 'paper' and user_choice == 'scissors':
        #print(scissors_message)
        winner = 'player'

    elif comp_choice == 'paper' and user_choice == 'rock':
        #print(paper_message)
        winner = 'computer'

    elif comp_choice == 'rock' and user_choice == 'paper':
        #print(paper_message)
        winner = 'player'

    return winner



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()

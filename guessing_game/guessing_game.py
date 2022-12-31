"""Game for guessing which cup has the ball"""

from random import shuffle

def return_random(input_list):
    """returns a random element of a list"""
    shuffle(input_list)
    return input_list[0]

def run_game():
    """play the guessing game"""
    input_guess = 0
    answer = return_random([1,2,3])
    print('''
    New Game! Guess where the ball is!
    _______   _______  _______
    |     |   |     |  |     |
    |  1  |   |  2  |  |  3  |
    |_____|   |_____|  |_____|

       ?         ?        ?
    ''')
    input_guess = 0
    while True:
        try:
            input_guess = int(input())
            if input_guess == answer:
                print(f'You win! The answer was {answer}')
                return
            if input_guess not in {1,2,3}:
                print('ERROR - Not in range! You must guess a number from 1-3\nGuess again!')
            else:
                print('Nope! Guess again.')
        except ValueError:
            print('ERROR - Not an integer! You must guess a number from 1-3\nGuess again!')

run_game()

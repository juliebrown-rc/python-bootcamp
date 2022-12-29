# Game for guessing which cup has the ball

from random import shuffle

def return_random(list):
    shuffled = list
    shuffle(list)
    return shuffled[0]

def run_game():
    x = 0
    answer = return_random([1,2,3])
    print('''
    New Game! Guess where the ball is!
    _______   _______  _______
    |     |   |     |  |     |
    |  1  |   |  2  |  |  3  |
    |_____|   |_____|  |_____|

       ?         ?        ?
    ''')
    x = 0
    while True:
        try:
            x = int(input())
            if x == answer:
                print(f'You win! The answer was {answer}')
                return
            elif x not in {1,2,3}:
                print('ERROR - Not in range! You must guess a number from 1-3\nGuess again!')
            else:
                print('Nope! Guess again.')
        except ValueError:
            print('ERROR - Not an integer! You must guess a number from 1-3\nGuess again!')

run_game()
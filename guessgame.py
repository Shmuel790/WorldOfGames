import random
from utils import screen_cleaner

def play(difficulty):
    screen_cleaner()
    print('\nWelcome to the Guess Game \n')
    secret_number = random.randint(1, difficulty)
    choose_number = int(input(f'Guess a number between 1 and {difficulty + 1}: '))

    def between(choose_number, difficulty):
        if 1 <= choose_number <= difficulty:
            return True
        else:
            print(f'Please enter a number between 1 and {difficulty + 1}. \n')

    def get_guess_from_user():
        while True:
            try:
                user_choose = between(choose_number, difficulty + 1)
                if user_choose:
                    return choose_number
                raise ValueError()
            except ValueError:
                return get_guess_from_user()

    def compare_results():
        if secret_number == choose_number:
            return True
        else:
            return False

    get_guess_from_user()
    compare_results()

    if compare_results():
        print('You guessed right! Nice Done!')
    else:
        print('You guessed wrong! Better luck next time.')
import random
import time
from utils import screen_cleaner

random_list = []
user_list = []


def play(difficulty):
    screen_cleaner()
    print('\nWelcome to the Memory Game \n')

    def generate_sequence():
        for i in range(0, difficulty):
            number = random.randint(1, 101)
            random_list.append(number)
            random_list.sort()
        print(random_list)
        time.sleep(0.7)
        screen_cleaner()

    def get_list_from_user():
        print('Enter the right numbers of the list you saw \n')
        for i in range(0, difficulty):
            user_type = int(input('Enter your number: '))
            user_list.append(user_type)

    def is_list_equal():
        if random_list == user_list:
            return True
        else:
            return False

    generate_sequence()
    get_list_from_user()
    is_list_equal()

    if is_list_equal():
        print(f'CORRECT!!! The list was {random_list}')
    else:
        print(f'You lost! The list was {random_list}. Better luck next time')
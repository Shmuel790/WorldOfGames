from live import load_game
from live import welcome


name = input('What is your name? ')
print(welcome(f'{name}'))
load_game()
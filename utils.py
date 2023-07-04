import os
import platform
import time

scores_file_name = 'scores.txt'

bad_return_code = '404 - score not found'

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('', end='\r')

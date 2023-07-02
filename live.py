import time
import memorygame
import guessgame
import currencyroulettegame

global difficulty, game_choose

def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG) \nHere you can find many cool games.\n'

def load_game():
    print('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    while True:
        try:
            game_choose = int(input('\nPlease insert a number between 1 - 3: '))
            while 3 < game_choose or game_choose < 1:
                game_choose = int(input('\nPlease insert a number between 1 - 3: '))
            difficulty = int(input('\nPlease choose game difficulty from 1 to 5: '))
            while 5 < difficulty or difficulty < 1:
                difficulty = int(input('\nPlease insert a number between 1 - 5: '))
        except ValueError:
            print('\nEnter just numbers please, not letters, words ,etc...')
            continue

        if game_choose == 1:
            print('\nYou chose the Memory Game! Enjoy it!')
            time.sleep(2)
            memorygame.play(difficulty)
        if game_choose == 2:
            print('\nYou chose the Guess Game! Enjoy it!')
            time.sleep(2)
            guessgame.play(difficulty)
        if game_choose == 3:
            print('\nYou chose the Currency Roulette Game! Enjoy it!')
            time.sleep(2)
            currencyroulettegame.play(difficulty)

        return difficulty, game_choose
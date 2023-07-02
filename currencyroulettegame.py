import random
import os.path as op
import urllib.request
from datetime import date
from currency_converter import ECB_URL, CurrencyConverter

filename = f"ecb_{date.today():%Y%m%d}.zip"
if not op.isfile(filename):
    urllib.request.urlretrieve(ECB_URL, filename)
CurrencyConverter(filename)


def play(difficulty):
    def get_money_interval():
        print('\nWelcome to the Currency Roulette!\n')
        global current
        global number
        currency = CurrencyConverter()
        current = currency.convert(1, 'USD', 'ILS')
        number = random.randint(1, 100)

    def get_guess_from_user():
        user_number = float(input(f'How much is {number} USD in ILS? '))
        a = between(difficulty, user_number)
        print(a)

    def between(difficulty, user_number):
        total = number * current
        print(f'${number} in ILS is {total} \n')
        if (total - (5 - difficulty)) <= user_number <= total + (5 - difficulty):
            return True
        else:
            return False

    get_money_interval()
    get_guess_from_user()
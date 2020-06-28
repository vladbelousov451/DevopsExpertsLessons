

import requests
import json
import random


response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")

json_data = json.loads(response.text)
ShekelCurrncy = json_data["rates"]['ILS']


def get_money_interval(ShekelCurrncy, t, d):
    afterExchange = t * ShekelCurrncy
    RandomNum = random(afterExchange - (5 - d), afterExchange + (5 - d))
    return RandomNum


def get_guess_from_user(UsDAmount):
    Guessed_Number = input(f" Print number for {UsDAmount} ")


def play():
    pass

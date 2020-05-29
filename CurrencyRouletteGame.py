

import requests
import json


response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")

json_data = json.loads(response.text)
ShekelCurrncy = json_data["rates"]['ILS']


def get_money_interval():
    print("I dont understand nothing")
    pass





def get_guess_from_user():
    pass





def play():
    pass

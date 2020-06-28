##### Functions ######

import MemoryGame
import GuessGame
import random


class WorldOfGamesGame():
    def __init__(self):
        self.l = []



    def welcome(self , name):
        print (f"  Hello {name}  and welcome to the World of Games (WoG).\n  Here you can find many cool games to play. ")

    def loadgame(self):
        game_type = input(
            """
        Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                            guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS

            Write Your answer here  : 


            """
        )
        if (int(game_type) >= 1 and int(game_type) <= 3):
            game_difficulty = int(self.get_game_difficulty())
            if int(game_type) == 1:
                MemoryGame == MemoryGame()
                MemoryGame.play(game_difficulty)
            elif int(game_type) == 2:
                GuessGame == GuessGame()
                GuessGame.play(game_difficulty)
            else:
                print("print number that i want you to print")
                self.loadgame()

    def get_game_difficulty(self):
        game_difficulty = input("Please choose game difficulty from 1 to 5: ")
        if (int(game_difficulty) >= 1 and int(game_difficulty) <= 5):
            return game_difficulty




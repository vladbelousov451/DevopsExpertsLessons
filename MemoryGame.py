
import random


class MemoryGame:
    def __init__(self):
        self.l = []



    def generate_sequence(self , difficulty):
        List_number = []
        for x in range(difficulty):
            Rand_number = random.randint(1 , 101 )
            List_number.append(Rand_number)
        return  List_number

    def get_list_from_user(self ,difficulty):
        List_number = []
        for x in range(difficulty):
            Alerted_number = input("Please Print the number you see below")
            List_number.append(Alerted_number)
        return  List_number


    def is_list_equal(self , Generated_list , Alrted_list):
        if(Generated_list == Alrted_list):
            return True
        else:
            return False


    def play(self , difficulty):
        print("Welcome to the Memory Game ")
        Generated_list = self.generate_sequence(difficulty)
        Alrted_list = self.get_list_from_user()
        Answer = self.is_list_equal(Generated_list , Alrted_list)
        return Answer




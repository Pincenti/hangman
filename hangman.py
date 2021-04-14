import random



secret_list = ["apple", "pear", "banana", "kiwi", "orange", "grape", "mango", "watermelon", "cherry", "blueberry"]


class Display:
    pass


class Player:
    pass


class Word:
    def __init__(self, secretword):
        secretword = secretword
        
    def random_word(self):
        print(random.choice(secret_List))
        
    

   

class Game:
    print("Welcome to guess the word game!")
    confirmed = True
    if confirmed == True:
        ask = input("\nType 'Ready' to play or 'quit' to quit ").lower()
        if ask == "quit":
            confirmed == False
        if ask == 'ready':
            print("\nTime to play guess the word game!")
            print("\nPicking word randomly.....")
        play = True
        while play:
            word = random.choice(secret_list)
            print(word)
            secret_word = len(word)
            print(secret_word)
            
            play = False
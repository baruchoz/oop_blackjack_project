import random

class Blackjack:

    def __init__(self):
        pass

class Card:
   
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Method to print out card
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        print("{} of {}".format(self.value, self.suit))

class Deck:
    
    def __init__(self):
        self.cards = [] # Empty list to append to 
        self.build() # Method to create a deck
    
    # Generate 52 Cards
    def build(self):
        
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]: # We create a for loop that will loop “suit” through ["Spades", "Clubs", "Diamonds", "Hearts"].
            for value in range(1,14): # We create another for loop within the first for loop that will loop through values in range(1,14)
                self.cards.append(Card(suit, value))

class Player:
    
    def __init__(self):
        pass

class User(Player):
    pass

class Dealer(Player):
    pass

class PlayGame:
    
    def __init__(self):
        pass
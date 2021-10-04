import random

class Card:
   
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

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

        print("{} of {}".format(val, self.suit))

class Deck:
    def __init__(self):
        self.cards = [] # Empty list to append to 
        self.build() # Method to create a deck
    
    # Generate 52 Cards
    def build(self):
        # s== suit. v == value
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]: # For loop that will loop “suit” through ["Spades", "Clubs", "Diamonds", "Hearts"].
            for v in range(1,14): # For loop within the first for loop that will loop through values in range(1,14)
                self.cards.append(Card(s, v))
    
    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            card.show()

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Deal a card
    def deal(self):
        return self.cards.pop()

class Player:   
    def __init__(self):
        pass
class User(Player):
    pass

class Dealer(Player):
    pass

class Game:
    
    def __init__(self):
        pass

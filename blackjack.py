import random

SUITS = ['♠︎', '♣︎', '♥︎', '♦︎']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    # pop() method removes the last item from list, but also returns it (essentially shorthand way of removing the top card from deck and simulates dealing cards to players during game)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
    
   

# THIS PART CONFUSES ME, ASK FOR EXPLANATION IN CLASS TOMORROW
# class Game:
#     def __init__(self):
#         self.player = None
#         self.dealer = None
#         self.deck = None
#         self.setup()
#         # calling the Game class's setup function

#     def setup(self):
#     # literally_any_word = name of class
#         self.deck = Deck()
#         # calls line 13
#         self.deck.add_cards()
#         # calls line 16
#         for card in self.deck.cards:
#             print(card)
#             # calls the __str__ method for each card


new_game = Game()
# created the game and the deck with cards

# TODO
# make a player, like we did with Deck ✅
# make a dealer, also like we did with Deck
# play
# shuffle deck
# deal cards
# player's turn (hit/stay)
# calculate score from cards in hand
# dealer's turn
# calculate score from cards in hand
# who won/lost/busted/21
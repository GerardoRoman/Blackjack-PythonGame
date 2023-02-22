import random

# Constants
SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()
    
class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        
    def add_card(self, card):
        self.hand.append(card)
        self.score += self.card_value(card)
        
    def card_value(self, card):
        if card.rank in ['K', 'Q', 'J']:
            return 10
        elif card.rank == 'A':
            return 11
        else:
            return int(card.rank)
        
    def adjust_for_ace(self):
        for card in self.hand:
            if card.rank == 'A' and self.score > 21:
                self.score -= 10
                
class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0
        
    def add_card(self, card):
        self.hand.append(card)
        self.score += self.card_value(card)
        
    def card_value(self, card):
        if card.rank in ['K', 'Q', 'J']:
            return 10
        elif card.rank == 'A':
            return 11
        else:
            return int(card.rank)
        
    def adjust_for_ace(self):
        for card in self.hand:
            if card.rank == 'A' and self.score > 21:
                self.score -= 10
                
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        
    def deal_initial_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        
    def player_turn(self):
        while self.player.score < 21:
            print(f"\nYour hand: {[str(card) for card in self.player.hand]}")
            print(f"Your score: {self.player.score}")
            choice = input("Do you want to hit or stand? (h/s) ")
            if choice == 'h':
                self.player.add_card(self.deck.deal_card())
                self.player.adjust_for_ace()
            else:
                break
                
    def dealer_turn(self):
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.deal_card())
            self.dealer.adjust_for_ace()
            
    def determine_winner(self):
        print(f"\nYour hand: {[str(card) for card in self.player.hand]}")
        print(f"Your score: {self.player.score}")
        print(f"\nDealer's hand: {[str(card) for card in self.dealer.hand]}")
        print(f"Dealer's score: {self.dealer.score}")
        
        if self.player.score > 21:
            print

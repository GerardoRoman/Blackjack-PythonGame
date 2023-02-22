import random

SUITS = ['♠︎', '♣︎', '♥︎', '♦︎']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card: # represents a standard playing card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck: # represents a deck of standard playing cards
    def __init__(self):
        self.cards = []

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self): # shuffles deck of cards
        random.shuffle(self.cards)
        
    def deal_card(self): # deals a single card from deck
        return new_game.deck.cards.pop()
    # pop() method removes the last item from list, but also returns it (shorthand way of removing the top card from deck and simulates dealing cards to players during game)
    
    

class Player: # represents a player in the game 
    def __init__(self):
        self.name = input("Enter player name: ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is the player'
    
    def turn(self):
        while True:
            print(f"\n{self.name}'s hand: ") # \n represents new line break for a cleaner look
            for card in self.hand:
                print(card)
            print(f"Total: {self.calculate_hand_value()}")
            decision = input("\nDo you want to hit or stay? ")
            if decision.lower() == 'hit':
                pass
                # print(F"{self.name} busts!")
                # return 'bust'
            else:
                return 'stay'
            
    def calculate_hand_value(self):
  
        hand_value = 0
        aces = 0
        for card in self.hand:
            if card.rank == 'A':
                aces += 1
            elif card.rank in ['K', 'Q', 'J']:
                hand_value += 10
            else:
                hand_value += card.rank
        for i in range(aces):
            if hand_value + 11 > 21:
                hand_value += 1
            else:
                hand_value += 11
        return hand_value


class Dealer(Player): # inherits from Player, init will be the same but turn will be different # everything is the same as player, unless you write it differently in here
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
    
    def __str__(self):
        return f'{self.name} is the dealer'
    
    def turn(self):
        while self.calculate_hand_value() < 17:
            card = new_game.deck.deal_card()
            self.hand.append(card)
            if self.calculate_hand_value() > 21:
                print(f"{self.name} busts!")
                return 'bust'
            else:
                return 'stay'


class Game: 
    def __init__(self):  # can set default values in the signature line, like 'deck=None'
        self.player = Player()  # the value of self.player is an instance of the class Player
        self.dealer = Dealer()
        self.setup()  # calling the Game class's setup function

    def setup(self):
        self.deck = Deck()
        self.deck.add_cards()
        
    def play_game(self):
        print("Welcome to Blackjack!")
        
        self.deal()
        
    def deal(self):
        self.deck.shuffle()
    
        while len(self.player.hand) < 2 and len(self.dealer.hand) < 2:
            
            self.player.hand.append(self.deck.deal_card())
            self.dealer.hand.append(self.deck.deal_card())
            
        print("\nDealer's up card:")
        print(self.dealer.hand[0])
        print("\nPlayer's cards:")
        print(self.player.hand[0], self.player.hand[1])
        
    def player_turn(self):
        result = self.player.turn(self.deck)
        if result == 'bust':
            self.end_game(self.dealer)
        else:
            self.dealer_turn()
    
    def dealer_turn(self):
        result = self.dealer.turn(self.deck)
        if result == 'bust':
            self.end_game(self.player)
        else:
            self.end_game()
            # player's turn
            self.player_turn()
            
            # dealer's turn
            self.dealer_turn()

# sets game-ending parameters
    def end_game(self, winner=None):
        
    # print player's hand and total
        print(f"\n{self.player.name}'s hand:")
        for card in self.player.hand:
            print(card)
        print(f"Total: {self.player.calculate_hand_value()}")
        
    # print dealer's hand and total
        print(f"\n{self.dealer.name}'s hand:")
        for card in self.dealer.hand:
            print(card)
        print(f"Total: {self.dealer.calculate_hand_value()}")
    
    # determine winner
        player_total = self.player.calculate_hand_value()
        dealer_total = self.dealer.calculate_hand_value()
        
        if player_total > 21:
            print("Dealer wins - Player busts!")
        elif dealer_total > 21:
            print("Player wins - Dealer busts!")
        elif player_total > dealer_total:
            print("Player wins!")
        elif dealer_total >= player_total:
            print("Dealer wins!")
        # else:
        #     print("It seems we have a tie!")
    
            
            # ask to play again
        play_again = input("\n Would you like to play again? (y/n) ")
        if play_again.lower() == 'n':
            print("Have a nice life!")
        else: 
            new_game.setup()
            new_game.play_game()

# Start Game
new_game = Game()
new_game.setup()
new_game.play_game()









# # new_game.player_turn()
# # new_game.deck.shuffle()
# card = new_game.deck.deal_card()
# new_game.dealer.hand.append(card)
# card = new_game.deck.deal_card()
# new_game.dealer.hand.append(card)
# print(new_game.dealer)
# for card in new_game.dealer.hand:
#     print(card)

# card = new_game.deck.deal_card()
# new_game.player.hand.append(card)
# card = new_game.deck.deal_card()
# new_game.player.hand.append(card)
# print(new_game.player)
# for card in new_game.player.hand:
#     print(card)

# TODO
# ✅ make a player, like we did with Deck 
# ✅ make a dealer, also like we did with Deck
# play
# ✅ shuffle deck 
# ✅ deal cards
# player's turn (hit/stay)
# calculate score from cards in hand
# dealer's turn
# calculate score from cards in hand
# who won/lost/busted/21
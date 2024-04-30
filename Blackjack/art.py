import art
import random

class Blackjack():

    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.game_state = True
        self.player_score = 0
        self.dealer_score = 0

    def loading_screen(self):
        print(art.loading_screen)
    
    def init_game(self):
        self.deck = self.create_deck() # initialize the deck

    # create a deck of cards. Each card will be a dictionary with the key being the card and the value being the number of cards in the deck
    def create_deck(self):
        self.deck.append({'A': 4})
        [(self.deck.append({i:4})) for i in range(2, 11)]
        [(self.deck.append({card:4})) for card in ['J', 'Q', 'K']]

        return self.deck
    
    # reduce the amount of cards in the deck by 1 for the card that was drawn
    def remove_card(self, drawn):
        [((self.deck[card]) - 1) for card in self.deck if drawn == card and self.deck[card] > 0]
        pass

    def draw_card(self)->int:
        deck = []

        # construct a list of what the current deck looks like
        for card in self.deck:
            if card in ['A', 'J', 'Q', 'K']:
                if card == 'A':
                    deck.extend([11] * self.deck[card])
                else:
                    deck.extend([10] * self.deck[card])
            else:
                deck.extend([card] * self.deck[card])
        
        # draw a card from the deck
        rand_index = random.randint(0, len(deck) - 1)

        # remove from actual deck to help prepare for next dealing of cards
        # -- create a mapping while extending list to see where index currently is

        card = deck[rand_index]
        return card

    def calculate_score(self, dealer, player):
        pass
        
    pass

# ace is an 11 or 1
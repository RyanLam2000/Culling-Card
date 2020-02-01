from card import Card
import random


def get_card_type(n: int, deck: {str:int}):
    for key in deck:
        if deck[key] >= n:
            return key
        n -= deck[key]

class Deck:
    def __init__(self):
        # Maps types of Cards to how many of each remain in the deck
        deck = dict()
        deck['Attack'] = 5
        deck['Defend'] = 3
        deck['Draw'] = 2
        self.deck = deck
    
    
    # Number of remaining cards in the deck
    def __len__(self):
        return sum(self.deck.values())
    
    
    def draw(self):
        # Determine what kind of Card will be drawn
        num_remaining = len(self)
        if (num_remaining == 0):
            return
        
        rand = random.randint(1, num_remaining)
        card_type = get_card_type(rand, self.deck)
        self.deck(card_type) -= 1
        
        # Create and return the appropriate Card
        return Card(card_type)
    
    
    def drawN(self, num_cards: int):
        cards = []
        for i in range(min(num_cards, len(self))):
            cards.append(self.draw)
            
        return cards
    
    
    def merge(self, cards: [Card]):
        for card in cards:
            card_type = card.type
            self.deck[card_type] += 1
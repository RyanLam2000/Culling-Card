from card import Card
from cards.blue_attack import BlueAttack
from cards.red_attack import RedAttack
from cards.green_attack import GreenAttack
from cards.defend_card import DefendCard
from cards.draw_card import DrawCard

import random


def add_new_cards(deck:[Card], card_type, num):
    for i in range(num):
        deck.append(card_type(i))
        
def update_card_slots(hand):
    for i in range(len(hand)):
        hand[i].set_slot(i)

class Deck:
    def __init__(self):
        # Store Cards remaining in the deck
        # Cards are drawn from the back of the list
        deck = list()
        add_new_cards(deck, BlueAttack, 2)
        add_new_cards(deck, RedAttack, 2)
        add_new_cards(deck, GreenAttack, 2)
        add_new_cards(deck, DefendCard, 3)
        add_new_cards(deck, DrawCard, 2)

        random.shuffle(deck)
        self.deck = deck
        
    # Number of remaining cards in the deck
    def __len__(self):
        return len(self.deck)
    
    
    def draw(self, hand, discard):
        if (len(self) == 0):
            self.merge(discard)
            discard.clear()
        if (len(hand) == 5):
            discard.append(self.deck.pop(-1))
        else:
            hand.append(self.deck.pop(-1))
            
        update_card_slots(hand)
    
    
    def draw_n(self, num_cards: int, hand, discard):
        for i in range(num_cards):
            self.draw(hand, discard)

        
    
    def merge(self, cards: [Card]):
        self.deck.extend(cards)
        random.shuffle(self.deck)
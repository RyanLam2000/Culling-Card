# example usage of deck, hand, discard, drawing
from card import Card
from deck import Deck
import pygame

deck = Deck()
hand = []
discard = []

drawn_cards = deck.draw(5) # returns list
hand.extend(drawn_cards)

while (True):
    while (len(hand) > 0):
        discard.append(hand.pop(0)) # Simulate using/removing cards from hand
        
    hand.extend(deck.drawN(5)) # may be smaller than 5 if less than 5 cards remain
    num_drawn = len(hand)
    
    # Put discard pile back into deck
    if (num_drawn < 5):
        deck.merge(discard)
        discard = []
        
        # Cards left to draw
        to_draw = 5 - num_drawn
        for i in range(to_draw):
            hand.extend(deck.drawN(to_draw))
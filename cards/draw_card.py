from card import Card

class DrawCard(Card):
    def __init__(self):
        self.en_cost = 20
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        deck.draw_n(2, hand, discard)
        drawn_cards = deck.draw_n(2)
        hand.extend(drawn_cards)
        num_drawn = len(hand)
        
    def retract(self):
        super().retract()

    

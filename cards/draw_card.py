from card import Card

class DrawCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        drawn_cards = deck.draw_n(2,hand,discard)
#         hand.extend(drawn_cards)
        num_drawn = len(hand)
        
    def retract(self):
        super().retract()

    

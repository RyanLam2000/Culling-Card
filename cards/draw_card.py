from card import Card

class DrawCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        
    def retract(self):
        super().retract()

    

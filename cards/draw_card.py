from card import Card

class DrawCard(Card):
    def __init__(self, slot = -1):
        super().__init__(slot = slot, img = "Vase_Of_Avarice.jpg")
        self.en_cost = 1
    
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        deck.draw_n(2, hand, discard)
        self.en_cost = 1
        
    def retract(self):
        super().retract()

    

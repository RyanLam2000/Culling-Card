from card import Card

class DefendCard(Card):
    def __init__(self, slot = -1):
        super().__init__(slot = slot, img = "Shield_Up.jpg")
        self.en_cost = 1
    
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        p.defence += 2
    
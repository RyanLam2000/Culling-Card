from card import Card

class DefendCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        p.defence += 5
        self.en_cost = 15
    def retract(self):
        super().retract()
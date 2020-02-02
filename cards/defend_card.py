from card import Card

class DefendCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked()
        p.defence += 5

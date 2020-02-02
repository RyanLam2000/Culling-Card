from card import Card

class DefendCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        p.defence += 5

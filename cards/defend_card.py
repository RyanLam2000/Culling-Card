from card import Card

class DefendCard(Card):
    def clicked(self, p, mob):
        p.defence += 5

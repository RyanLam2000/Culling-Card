from card import Card

class DefendCard(Card):
    def clicked(self, p, mob):
        super().clicked()
        p.defence += 5

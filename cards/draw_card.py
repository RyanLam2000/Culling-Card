from card import Card

class DrawCard(Card):
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked()
        drawn_cards = deck.draw_n(2)
        hand.extend(drawn_cards)
        num_drawn = len(hand)
from card import Card

class DrawCard(Card):
    def clicked(self, p, mob):
        super().clicked()
        print("POT OF GREED ALLOWS ME TO DRAW TWO MORE CARDS. I WILL START MY TURN BY PLAYING POT OF GREED WHICH ALLOWS ME TO DRAW TWO MORE CARDS.")
        
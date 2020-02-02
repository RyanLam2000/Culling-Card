from card import Card

class BlueAttack(Card):
    def __init__(self, slot = -1):
        super().__init__(img = "attack_card_blue.jpg")
        self.en_cost = 10
        
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        if mob.type == "green":
            mob.health -= 3
        elif mob.type == "red":
            mob.health -= 8
        else:
            mob.health -= 5
        mob.update()
    def retract(self):
        super().retract()
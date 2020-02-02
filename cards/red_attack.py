from card import Card

class RedAttack(Card):
    def __init__(self, slot = -1):
        super().__init__(slot = slot, img = "Card_Throw.jpg")
        self.en_cost = 1
        
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked(p, mob, deck, hand, discard)
        if mob.type == "blue":
            mob.health -= 3
        elif mob.type == "green":
            mob.health -= 8
        else:
            mob.health -= 5
        mob.update()
        
    def retract(self):
        super().retract()
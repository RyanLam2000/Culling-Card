from card import Card

class RedAttack(Card):
    def __init__(self, slot = -1):
        super().__init__(slot = slot, img = "attack_card_red.jpg")
        
    def clicked(self, p, mob, deck, hand, discard):
        super().clicked()
        if mob.type == "blue":
            mob.health -= 3
        elif mob.type == "green":
            mob.health -= 8
        else:
            mob.health -= 5
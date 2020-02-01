from card import Card

class GreenAttack(Card):
    def clicked(self, p, mob):
        if mob.type == "red":
            mob.health -= 3
        elif mob.type == "blue":
            mob.health -= 8
        else:
            mob.health -= 5
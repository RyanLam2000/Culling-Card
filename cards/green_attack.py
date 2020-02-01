import card

class GreenAttack(card):
    def clicked(self, mob):
        if mob.type == "red":
            mob.health -= 3
        elif mob.type == "blue":
            mob.health -= 8
        else:
            mob.health -= 5
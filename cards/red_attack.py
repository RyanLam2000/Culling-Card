import card

class redAttack(card):
    def clicked(self, p, mob):
        if mob.type == "blue":
            mob.health -= 3
        elif mob.type == "green":
            mob.health -= 8
        else:
            mob.health -= 5
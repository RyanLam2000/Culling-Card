import card

class BlueAttack(card):
    def clicked(self, mob):
        if mob.type == "green":
            mob.health -= 3
        elif mob.type == "red":
            mob.health -= 8
        else:
            mob.health -= 5
from card import Card


class BlueAttack(Card):
    icon = 
    def clicked(self, p, mob):
        if mob.type == "green":
            mob.health -= 3
        elif mob.type == "red":
            mob.health -= 8
        else:
            mob.health -= 5
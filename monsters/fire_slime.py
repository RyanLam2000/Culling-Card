from enemy import Enemy

class FireSlime(Enemy):
    def __init__(self):
        super("fire_slime.png")
        self.hp = 10
        self.power = 2
        self.type = "red"
from enemy import Enemy

class Fire_slime(Enemy):
    def __init__(self):
        super()
        self.hp = 10
        self.power = 2
        self.type = "red"
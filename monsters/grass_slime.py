from enemy import Enemy

class GrassSlime(Enemy):
    def __init__(self, multiplier = 0):
        super().__init__(11, 3, 'green', "PoisonSlime.png", multiplier)
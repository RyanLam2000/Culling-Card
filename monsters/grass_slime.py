from enemy import Enemy

class GrassSlime(Enemy):
    def __init__(self):
        super().__init__(10, 2, 'green', "PoisonSlime.png")
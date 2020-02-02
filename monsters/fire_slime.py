from enemy import Enemy

class FireSlime(Enemy):
    def __init__(self, multiplier = 0):
        super().__init__(9, 5, 'red', "FireSlime.png", multiplier)
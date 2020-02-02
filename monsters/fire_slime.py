from enemy import Enemy

class FireSlime(Enemy):
    def __init__(self):
        super().__init__(10, 2, 'red', "FireSlime.png")
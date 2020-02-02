from enemy import Enemy

class WaterSlime(Enemy):
    def __init__(self):
        super().__init__(10, 2, 'blue', "IceSlime.png")
import random
from monsters.fire_slime import FireSlime

class GetEnemy:
    def __init__(self):
        enemy_list = []
        enemy_list.append(FireSlime)
        self.enemy_list = enemy_list
        
    def get_enemy(self):
        rand = random.randint(0, len(self.enemy_list))
        enemy_class = self.enemy_list[rand]
        return enemy_class()
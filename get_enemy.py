import random
from monsters.fire_slime import FireSlime
from monsters.water_slime import WaterSlime
from monsters.grass_slime import GrassSlime


def get_enemy():
    enemy_list = [FireSlime, WaterSlime, GrassSlime]
    rand = random.randint(0, len(enemy_list) - 1)
    enemy_class = enemy_list[rand]
    return enemy_class()
# Basic script to get player and enemy health from screenshot

import math
from PIL import Image

# Total health pixels = 396
full_health = 396
# Health bar ends
player_health_full = (749, 126)
player_health_zero = (1126, 126)
enemy_health_full = (1666, 126)
enemy_health_zero = (1289, 126)
# Health bar pixel lists
player_health_pixels = zip(range(1126, 748), 396*[126])
enemy_health_pixels = zip(range(1289, 1667), 396*[126])


# The R value of pixels in health bar which indicate hp greater than current hp is 49
def get_player_health():
    for pixel in player_health_pixels:
        pixel_r = px[pixel[0], pixel[1]][0]
        if pixel_r is 49:
            health = math.fabs(pixel[0] - player_health_zero[0])
            return health
    return full_health


def get_enemy_health():
    for pixel in enemy_health_pixels:
        pixel_r = px[pixel[0], pixel[1]][0]
        if pixel_r is 49:
            health = math.fabs(pixel[0] - enemy_health_zero[0])
            return health
    return full_health


img = Image.open("Screenshot1.png")
px = img.load()

enemy_health = get_enemy_health()
print("\nEnemy health:")
print(enemy_health)
print(enemy_health/full_health * 100)
player_health = get_player_health()
print("\nPlayer health:")
print(player_health)
print(player_health/full_health * 100)

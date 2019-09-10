# Basic script to get player and enemy health from screenshot

import cv2
import numpy as np
import math

# Total health pixels = 378
full_health = 378

# Health bar end pixels
player_health_full = (126, 749)
player_health_zero = (126, 1126)
enemy_health_full = (126, 1666)
enemy_health_zero = (126, 1289)

# Health bar pixel lists
player_health_pixels = zip(378*[126], range(1126, 748))
enemy_health_pixels = zip(378*[126], range(1289, 1667))


# The R value of pixels in health bar which indicate hp greater than current hp is 49
def get_player_health():
    for pixel in player_health_pixels:
        pixel_r = img.item(*pixel, 2)
        if pixel_r is 49:
            health = math.fabs(pixel[1] - player_health_zero[1])
            return health
    return full_health


def get_enemy_health():
    for pixel in enemy_health_pixels:
        pixel_r = img.item(*pixel, 2)
        if pixel_r is 49:
            health = math.fabs(pixel[1] - enemy_health_zero[1])
            return health
    return full_health


img = cv2.imread("Screenshot.png")

enemy_health = get_enemy_health()
print(enemy_health)
print(enemy_health/full_health * 100)
player_health = get_player_health()
print(player_health)
print(player_health/full_health * 100)

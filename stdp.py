import numpy as np
from map import print_map


if __name__ == "__main__":
    map = np.load("map.npy")
    width, height = map.shape
    print_map(map)
"""
. . . . . #
# . . # . .
. . . . . #
. # . # # .
# . . . . .
. . # # . .
"""

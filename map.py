import random
import numpy as np
from plot import path_plot


def generate_map(width, height, obstacle_ratio=0.2):

    grid = np.zeros((height, width), dtype=int)

    num_obstacles = int(width * height * obstacle_ratio)

    for _ in range(num_obstacles):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y, x] = 1

    return grid


def print_map(grid):
    for row in grid:
        print(" ".join("#" if cell == 1 else "." for cell in row))


if __name__ == "__main__":
    width, height = 6, 6
    game_map = generate_map(width, height, obstacle_ratio=0.3)
    path_plot(game_map, [], "map.png")

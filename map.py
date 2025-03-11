import random
import numpy as np


def generate_map(width, height, obstacle_ratio=0.2):
    """
    生成一个随机地图，包含障碍物。
    :param width: 地图宽度
    :param height: 地图高度
    :param obstacle_ratio: 障碍物占比 (0~1)
    :return: 生成的2D地图 (numpy array)
    """
    # 初始化地图，全为 0
    grid = np.zeros((height, width), dtype=int)

    # 计算障碍物数量
    num_obstacles = int(width * height * obstacle_ratio)

    # 随机放置障碍物
    for _ in range(num_obstacles):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        grid[y, x] = 1  # 注意索引 (y, x)

    return grid


def print_map(grid):
    """打印地图"""
    for row in grid:
        print(" ".join("#" if cell == 1 else "." for cell in row))


if __name__ == "__main__":
    # 示例使用
    width, height = 6, 6
    game_map = generate_map(width, height, obstacle_ratio=0.3)
    print_map(game_map)
    # np.save("map.npy", game_map)

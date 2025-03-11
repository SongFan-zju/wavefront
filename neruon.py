import numpy as np


class Weight:

    def __init__(self, src, dest, weight=0.5, trace=0):
        self.weight = weight
        self.trace = trace
        self.src, self.dest = src, dest

    def stdp(self):
        self.weight = self.weight + self.trace

    def _step_trace(self):
        self.trace /= 2


class Node:

    def __init__(self, pos_x, pos_y, flag=0, threshold=0.4):
        self.pos = (pos_x, pos_y)
        self.threshold = threshold
        self.flag = flag
        self.activate = 1
        self.input_wgt = []
        self.output_wgt = []


class Map:

    def __init__(self, map_value):
        self.width, self.height = map_value.shape
        self.pot = np.zeros((self.width, self.height))
        self.node = np.array([[Node(i, j, map_value[i][j]) for j in range(self.height)] for i in range(self.width)])
        self._init()

    def _init(self):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(self.width):
            for j in range(self.height):
                for k in move:
                    end_x, end_y = i + k[0], j + k[1]
                    if end_x < 0 or end_x >= self.width or end_y < 0 or end_y >= self.height:
                        continue
                    wgt = Weight((i, j), (end_x, end_y), 0.5)
                    self.node[i][j].output_wgt.append(wgt)
                    self.node[end_x][end_y].input_wgt.append(wgt)

    def step(self):
        temp_pot = np.copy(self.pot)
        cnt = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.pot[i][j] > self.node[i][j].threshold:
                    cnt += 1
                    for k in self.node[i][j].input_wgt:
                        k.stdp()
                    if self.node[i][j].activate == 1:
                        for k in self.node[i][j].output_wgt:
                            k.trace += 1
                            if self.node[k.dest[0]][k.dest[1]].flag == 1:
                                continue
                            temp_pot[k.dest[0]][k.dest[1]] += k.weight
                    temp_pot[i][j] = 0
                    self.node[i][j].activate = 0
        self.pot = temp_pot
        self._step_trace()
        return cnt

    def _step_trace(self):
        for i in range(self.width):
            for j in range(self.height):
                for k in self.node[i][j].input_wgt:
                    k._step_trace()


if __name__ == "__main__":
    map_value = np.load("map.npy")
    map = Map(map_value)
    start = (0, 0)
    end = (5, 5)
    map.pot[end[0]][end[1]] = 1
    while 1:
        ret = map.step()
        if ret == 0:
            break
    path = []
    path.append(start)
    while path[-1] != end:
        temp_start = path[-1]
        if map.node[temp_start].flag == 1:
            break
        input_wgt = map.node[temp_start[0]][temp_start[1]].input_wgt
        max_wgt = max(input_wgt, key=lambda x: x.weight)
        # print(max_wgt.weight)
        if map.node[max_wgt.src].flag == 1:
            break
        path.append(max_wgt.src)
    if path[-1] == end:
        for i in path:
            print(i, end="")
            if i != end:
                print("->", end="")
        print("\nSuccess!")
    else:
        print("Fail to find path!")
"""
. . . . . #
# . . # . .
. . . . . #
. # . # # .
# . . . . .
. . # # . .
"""

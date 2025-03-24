import matplotlib.pyplot as plt
import numpy as np


def to_plot_coords(y, x, rows):
    return (x, rows - 1 - y)


def path_plot(map, path, fig_path="path.png"):
    rows, cols = map.shape
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(-0.5, rows - 0.5)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    path_edges = set()

    for i in range(len(path) - 1):
        path_edges.add((path[i], path[i + 1]))

    for y in range(rows):
        for x in range(cols):
            cx, cy = to_plot_coords(y, x, rows)
            val = map[y][x]
            color = 'white' if val == 0 else 'black'
            ax.add_patch(plt.Circle((cx, cy), 0.3, facecolor=color, edgecolor='black', zorder=2))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    arrow_color = '#888888'

    for y in range(rows):
        for x in range(cols):
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols:
                    a = (y, x)
                    b = (ny, nx)
                    if (a, b) in path_edges:
                        continue
                    cx0, cy0 = to_plot_coords(*a, rows)
                    cx1, cy1 = to_plot_coords(*b, rows)

                    offset = 0.1
                    ox = -offset * dy
                    oy = offset * dx
                    dx_arrow = cx1 - cx0
                    dy_arrow = cy1 - cy0
                    ax.arrow(cx0 + ox,
                             cy0 + oy,
                             dx_arrow * 0.7,
                             dy_arrow * 0.7,
                             head_width=0.15,
                             head_length=0.15,
                             fc=arrow_color,
                             ec=arrow_color,
                             length_includes_head=True,
                             zorder=1)

    for (y0, x0), (y1, x1) in path_edges:
        cx0, cy0 = to_plot_coords(y0, x0, rows)
        cx1, cy1 = to_plot_coords(y1, x1, rows)
        dx = cx1 - cx0
        dy = cy1 - cy0
        ax.arrow(cx0,
                 cy0,
                 dx * 0.7,
                 dy * 0.7,
                 head_width=0.12,
                 head_length=0.12,
                 fc='red',
                 ec='red',
                 length_includes_head=True,
                 zorder=3)

    for i in path:
        cx, cy = to_plot_coords(*i, rows=rows)
        ax.add_patch(plt.Circle((cx, cy), 0.35, facecolor='blue', edgecolor='blue', linewidth=2, zorder=4))
    if fig_path != "":
        plt.savefig(fig_path)
    plt.show()


if __name__ == "__main__":
    map = np.load("example.npy")
    path_plot(map, [], "example.png")

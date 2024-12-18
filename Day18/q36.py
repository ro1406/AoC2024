"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q35.py (c) 2024
Desc: description
Created:  2024-12-18T05:07:25.614Z
Modified: 2024-12-18T05:24:10.427Z
"""

from collections import deque


def find_path(i, j, grid):
    steps = 0

    q = deque([(i, j, steps)])
    min_steps = float("inf")
    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]

    while q:
        x, y, steps = q.popleft()

        # Check goal
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            min_steps = min(min_steps, steps)

            continue

        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and grid[x + dx][y + dy] == "."
                and not visited[x + dx][y + dy]
            ):
                visited[x + dx][y + dy] = True
                q.append((x + dx, y + dy, steps + 1))

    return min_steps


grid = [["." for _ in range(71)] for __ in range(71)]

with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i < 1024:
            x, y = line.strip().split(",")
            grid[int(y)][int(x)] = "#"
        else:
            # Add wall and then call bfs and see if its possible
            x, y = line.strip().split(",")
            grid[int(y)][int(x)] = "#"
            min_steps = find_path(0, 0, grid)
            if min_steps == float("inf"):
                print("FOUND FIRST BLOCKER:")
                print(x,y)
                break

# for x in grid:
#     print(''.join(x))

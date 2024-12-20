"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q39.py (c) 2024
Desc: description
Created:  2024-12-20T05:52:50.169Z
Modified: 2024-12-20T11:08:55.414Z
"""

from collections import deque
from time import time

def find_path(i, j, grid):
    steps = 0
    curr_path = [(i, j)]
    q = deque([(i, j, steps, curr_path)])
    min_steps = float("inf")
    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    best_paths = []

    while q:
        x, y, steps, curr_path = q.popleft()

        # Check goal
        if grid[x][y] == "E":
            min_steps = min(min_steps, steps)
            best_paths.append(curr_path[:])
            continue

        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and grid[x + dx][y + dy] != "#"
                and not visited[x + dx][y + dy]
            ):
                visited[x + dx][y + dy] = True
                q.append((x + dx, y + dy, steps + 1, curr_path + [(x + dx, y + dy)]))

    return min_steps, best_paths


def count_walls(x1, y1, x2, y2, grid):
    num_walls = 0
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            if grid[i][j] == "#":
                num_walls += 1

    return num_walls


grid = []
with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
# print(grid)

# Find s
sx, si = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            sx, sy = i, j
            break


t0=time()
best_score, best_paths = find_path(sx, sy, grid)
print(f"{best_score=}")
print(f"Number of best paths: {len(best_paths)}")
best_path = best_paths[0]

ans = 0
for cheat_length in range(2, 21):
    print("Doing cheat_length =", cheat_length)
    for lag in range(100 + cheat_length, len(best_path), 2):
        # Try and lag the best_path by lag and compare
        for (a, b), (c, d) in zip(best_path, best_path[lag:]):
            # manhattan dist is the cheat length
            if abs(a - c) + abs(b - d) == cheat_length:
                ans += 1

print(ans)
print("Time taken:",time()-t0)

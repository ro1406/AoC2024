"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day10pt1.py (c) 2024
Desc: description
Created:  2024-12-10T12:46:29.159Z
Modified: 2024-12-11T04:11:39.526Z
"""

from collections import deque


def get_score(i, j):
    curr_value = 0
    q = [(i, j, curr_value)]
    ans_set = list()  # Use list instead of set - save everytime i reach a 9

    while q:
        x, y, curr_value = q.pop(0)
        if grid[x][y] == 9:
            ans_set.append((x, y, curr_value))
            continue

        # Add all neighbours that are at curr_value+1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == curr_value + 1:
                q.append((x + dx, y + dy, curr_value + 1))
    return ans_set


grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(map(int, line.strip())))
for x in grid:
    print(x)

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            # Start point
            ans_set = get_score(i, j)
            score = len(ans_set)
            ans += score
print(ans)

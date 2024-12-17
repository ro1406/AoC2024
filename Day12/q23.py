"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day12pt1.py (c) 2024
Desc: description
Created:  2024-12-12T04:36:13.353Z
Modified: 2024-12-12T07:14:47.388Z
"""

from time import time
from collections import deque

grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))


def inside(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_area(i, j, letter):
    q = deque([(i, j)])
    area = 0
    perimeter = 0
    while q:
        x, y = q.popleft()

        # Check if goal
        if grid[x][y] == letter:
            area += 1

        grid[x][y] = f"{letter}."

        temp_perimeter = 4
        # Add other neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if inside(x + dx, y + dy) and grid[x + dx][y + dy] == letter and (x + dx, y + dy) not in q:
                q.append((x + dx, y + dy))
            if inside(x + dx, y + dy) and (grid[x + dx][y + dy] == letter or grid[x + dx][y + dy] == f"{letter}."):
                temp_perimeter -= 1

        perimeter += temp_perimeter

    return area, perimeter


t0 = time()

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if "." not in grid[i][j]:
            # There is a valid letter so lets find the area and perimeter
            # print(grid[i][j],end=' ')
            area, perimeter = get_area(i, j, grid[i][j])
            # print(area, perimeter)
            ans += area * perimeter

print(ans)
print("Time taken:", time() - t0)

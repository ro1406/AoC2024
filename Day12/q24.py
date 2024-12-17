"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day12pt1.py (c) 2024
Desc: description
Created:  2024-12-12T04:36:13.353Z
Modified: 2024-12-12T11:10:43.015Z
"""

from time import time
from collections import deque
from copy import deepcopy

grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
original_grid=deepcopy(grid)

def inside(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_area(i, j, letter):
    q = deque([(i, j)])
    coordinates=set()
    area = 0
    perimeter = 0
    while q:
        x, y = q.popleft()
        coordinates.add((x,y))

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

    return area, coordinates


def find_num_consecutive_groups(arr,use_rows=True):
    ans=0
    curr_group=1
    for i in range(1,len(arr)):
        if use_rows:
            if arr[i][0]-arr[i-1][0]==1 and arr[i][1]==arr[i-1][1]:
                curr_group+=0
            else:
                ans+=curr_group
                curr_group=1
        else:
            if arr[i][1]-arr[i-1][1]==1 and arr[i][0]==arr[i-1][0]:
                curr_group+=0
            else:
                ans+=curr_group
                curr_group=1
    ans+=curr_group
    return ans


def get_perimeter(coordinates,letter):
    left=[]
    right=[]
    up=[]
    down=[]
    
    for i,j in coordinates:
        #Check left border
        if not inside(i,j-1) or inside(i,j-1) and original_grid[i][j-1]!=letter:
            left.append((i,j-1))
        #Check right border
        if not inside(i,j+1) or inside(i,j+1) and original_grid[i][j+1]!=letter:
            right.append((i,j+1))
        #Check top border
        if not inside(i-1,j) or inside(i-1,j) and original_grid[i-1][j]!=letter:
            up.append((i-1,j))
        #Check bottom border
        if not inside(i+1,j) or inside(i+1,j) and original_grid[i+1][j]!=letter:
            down.append((i+1,j))
    
    #Sort each array by i/j coordinate respectively
    left.sort(key=lambda x:(x[1],x[0]))
    right.sort(key=lambda x:(x[1],x[0]))
    
    up.sort(key=lambda x:(x[0],x[1]))
    down.sort(key=lambda x:(x[0],x[1]))
    print("Sorted borders:")
    print(left,right,up,down)

    #Find consecutive groups in each array
    left_ans = find_num_consecutive_groups(left)
    right_ans = find_num_consecutive_groups(right)
    up_ans = find_num_consecutive_groups(up,use_rows=False)
    down_ans = find_num_consecutive_groups(down,use_rows=False)
    print(f'{left_ans=}, {right_ans=}, {up_ans=}, {down_ans=}')
            
    return left_ans+right_ans+up_ans+down_ans


t0 = time()

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if "." not in grid[i][j]:
            letter = grid[i][j]
            # There is a valid letter so lets find the area and perimeter
            print(letter)
            area,coordinates = get_area(i, j, letter)
            print(coordinates)
            perimeter = get_perimeter(coordinates,letter)
            print(area,perimeter)
            print('-'*100)
            ans += area * perimeter
            
print(ans)
print("Time taken:", time() - t0)

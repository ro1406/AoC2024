"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day10pt1.py (c) 2024
Desc: description
Created:  2024-12-10T12:46:29.159Z
Modified: 2024-12-11T04:07:30.925Z
"""
from collections import deque

def get_score(i,j):
    curr_value=0
    q = [(i,j,curr_value)]
    ans_set=set()
    
    while q:
        x,y,curr_value=q.pop()
        # print('exploring:',x,y,curr_value)
        if grid[x][y]==9:
            ans_set.add((x,y,curr_value))
            continue
        
        #Add all neighbours that are at curr_value+1
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]==curr_value+1:
                q.append((x+dx,y+dy,curr_value+1))
        # print("after loop iter:",q,curr_value)
    return ans_set



grid=[]
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(list(map(int, line.strip())))
for x in grid:
    print(x)

# print(get_score(0,3))

ans=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==0:
            #Start point
            ans_set = get_score(i,j)
            score=len(ans_set)
            # print(f"Found 9, {i=},{j=}: {score=}")
            ans+=score
print(ans)
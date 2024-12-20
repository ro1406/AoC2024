"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q39.py (c) 2024
Desc: description
Created:  2024-12-20T05:52:50.169Z
Modified: 2024-12-20T07:22:23.706Z
"""
from collections import deque
def find_path(i,j,grid):
    steps=0
    curr_path=[(i,j)]
    q=deque([(i,j,steps,curr_path)])
    min_steps = float('inf')
    visited=[[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    best_paths=[]
    
    while q:
        x,y,steps,curr_path=q.popleft()
        
        #Check goal
        if grid[x][y]=='E':
            min_steps = min(min_steps,steps)
            best_paths.append((curr_path[:],min_steps))
            continue
        
        #Check neighbors
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]!='#' and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy]=True
                q.append((x+dx,y+dy,steps+1,curr_path+[(x+dx,y+dy)]))
        
    return min_steps,best_paths


grid=[]
with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
# print(grid)

#Find s
sx,si=0,0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='S':
            sx,sy=i,j
            break


best_score, best_paths = find_path(sx,sy,grid)
print(f"{best_score=}")
print(f"Number of best paths: {len(best_paths)}")


best_path,best_score = best_paths[0]

ans=0
pairs=set()
dic={}
for lag in range(102,len(best_path)):
    # print(lag)
    #Try and lag the best_path by lag and compare
    for (a,b),(c,d) in zip(best_path,best_path[lag:]):
        #If same row and 2 cols away with # in the middle
        # or IF some col and 2 rows away with # in the middle
        if (a==c and abs(b-d)==2 and grid[a][int((b+d)/2)]=='#') or (b==d and abs(a-c)==2 and grid[int((a+c)/2)][b]=='#'):
            pairs.add((a,b,c,d))
            if lag in dic:
                dic[lag].append(f'({a},{b}) & ({c},{d})')
            else:
                dic[lag]=[f'({a},{b}) & ({c},{d})']
            ans+=1

print(ans)
print(len(pairs))
for key in dic:
    print(f"{key}: {len(dic[key])}")
#1411 too high
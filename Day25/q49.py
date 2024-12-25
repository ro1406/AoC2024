"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q49.py (c) 2024
Desc: description
Created:  2024-12-25T04:48:07.113Z
Modified: 2024-12-25T05:17:16.378Z
"""

keys=[]
locks=[]


with open("input.txt",'r') as file:
    
    current_grid = []
    for line in file:
        line = line.strip()
        if line:
            current_grid.append(line)
        else:
            if current_grid:
                if all(x=='#' for x in current_grid[0]):
                    locks.append(current_grid)
                else:
                    keys.append(current_grid)
                current_grid = []
    # Add the last grid if the file doesn't end with a blank line
    if current_grid:
        if all(x=='#' for x in current_grid[0]):
            locks.append(current_grid)
        else:
            keys.append(current_grid)
            
            

# print('LOCKS:')
# for lock in locks:
#     for x in lock:
#         print(x)

# print('-'*100)
# print('KEYS:')
# for key in keys:
#     for x in key:
#         print(x)


def check(lock,key):
    if len(lock)!=len(key):
        print("row mismatch")
        return False
    if len(lock[0])!=len(key[0]):
        print("col mismatch")
        return False
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j]=='#' and key[i][j]=='#':
                #Collision
                return False
    return True

ans=0
for lock in locks:
    for key in keys:
        if check(lock,key):
            ans+=1

print(ans)
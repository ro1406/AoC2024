"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
pt1.py (c) 2024
Desc: description
Created:  2024-12-09T07:12:04.569Z
Modified: 2024-12-10T12:07:40.340Z
"""
from time import time
with open("input.txt", "r") as f:
    line = list(map(int, f.readlines()[0]))
# print(line)
original_line = line.copy()

#Prefix array to avoid doing sum(original_line[:empty_idx]) everytime
original_line_sum=[]
s=0
for x in line:
    s+=x
    original_line_sum.append(s)

t0=time()

# ID: index//2
# file: index%2==0
# empty: index%2==1

# Start from last file and distribute it into first few empty spaces
# Distributing means ans+= (file-empty)*ID*index
# Then file-=empty and update empty to the next empty space

ans = 0
file = 0
empty = 0
if len(line) % 2 == 0:
    for index in range(len(line) - 2, -1, -2):
        # Starting from last file
        file = int(line[index])
        empty_idx = len(line) - index
        while file > 0 and line[empty_idx] > 0:
            empty = int(line[empty_idx])
            ID = empty_idx // 2
            if file >= empty:
                ans += (file - empty) * ID * empty_idx
                line[empty_idx] = 0

            file -= empty
            empty_idx -= 2
else:
    #print("LENGTH IS ODD")
    
    for index in range(len(line) - 1, -1, -2):
        # Starting from last file
        file = int(line[index])
        ID = index // 2
        empty_idx = 1
        #Check if we can find an empty space with line[index]<=line[empty_idx]
        placed=False
        while 0 <= empty_idx < len(line) and empty_idx<index:
            empty = int(line[empty_idx])
            if empty >= file:
                # print(f"placed: {ID=}, {index=}, {file=}, {empty_idx=}")
                
                ans += sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(file))
                # ans += ID * ( (file-1)*file//2 + (sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx])*(file))
                # ans += ID * ( (file-1)*file//2 + (original_line_sum[empty_idx]+original_line[empty_idx]-line[empty_idx])*(file))
                # print(f"Adding {sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(file))} to ans")
                line[empty_idx] = empty - file
                placed=True
                # print(original_line)
                # print(line)
                break
            else:
                empty_idx += 2
        #012345678901234567890123456789012345678901
        #00992111777.44.333....5555.6666.....8888..
        
        #If we couldnt find a place to place this, then add the file to ans in current location
        if not placed:
            # print(f"not placed: {ID=}, {index=}, {file=}, {empty_idx=}")
            # print(original_line)
            # print(line)
            ans+=sum(ID*(i+sum(original_line[:index])) for i in range(file))
            # print(f"Adding {sum(ID*(i+sum(original_line[:index])) for i in range(file))} to ans")

        # print(ans)
        # print("-" * 100)

print(ans)
print("Time taken:",time()-t0)

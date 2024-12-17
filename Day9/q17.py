"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
pt1.py (c) 2024
Desc: description
Created:  2024-12-09T07:12:04.569Z
Modified: 2024-12-10T08:03:40.105Z
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

# arr=[-1]*sum(line)
# id=0
# arr_ptr = 0
# for i,x in enumerate(line):
#     if i%2==0:
#         #File
#         for j in range(x):
#             arr[arr_ptr]=id
#             arr_ptr+=1
#         id+=1
#     else:
#         #Empty space
#         arr_ptr+=x

# l,r=0,len(arr)-1
# while l<r:
#     #Left finds first empty location
#     while arr[l]!=-1: l+=1
#     #Right finds first filled location
#     while arr[r]==-1: r-=1
#     #Swap
#     arr[l],arr[r]=arr[r],arr[l]
#     l+=1
#     r-=1

# arr=[x if x!=-1 else 0 for x in arr]
# print(arr)

# ans=0
# for i,x in enumerate(arr):
#     ans+= i*x
# print(ans)


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
    empty_idx = 1
    for index in range(len(line) - 1, -1, -2):
        # Starting from last file
        file = int(line[index])
        ID = index // 2

        # #print(f"Doing, {ID=}, {index=},{file=},{empty_idx=}", end=" ")
        if empty_idx<index:
            # if file > 0 and 0 <= empty_idx < len(line) and line[empty_idx] > 0:
                #print("Entering while loop", end=" ")
            # else:
                #print("Skipped while loop")
            while line[index] > 0 and 0 <= empty_idx < len(line) and line[empty_idx] > 0 and empty_idx<index:
                file = int(line[index])
                #print(f"doing, {ID=}, {index=}, {file=}, {empty_idx=}")
                entered_while=True
                empty = int(line[empty_idx])
                if empty >= file:
                    #print(original_line)
                    #print(line)
                    # ans += sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(file))
                    # ans += ID * ( (file-1)*file//2 + (sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx])*(file))
                    ans += ID * ( (file-1)*file//2 + (original_line_sum[empty_idx]+original_line[empty_idx]-line[empty_idx])*(file))
                    
                    #print(f"empty>=file: adding {sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(file))} to ans")
                    line[empty_idx] = empty - file
                    line[index] = 0
                else:
                    # empty<file
                    #print(original_line)
                    #print(line)
                    # ans+= sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(empty))
                    ans += ID * ( (empty-1)*empty//2 + (original_line_sum[empty_idx]+original_line[empty_idx]-line[empty_idx])*(empty))
                    
                    #print(f"empty<file: adding {sum(ID*(i+sum(original_line[:empty_idx])+original_line[empty_idx]-line[empty_idx]) for i in range(empty))} to ans")
                    line[index] -= empty
                    line[empty_idx] = 0
                # #print(f"After updates, {index=},{file=},{empty_idx=},{line[empty_idx]=}")
                
                while 0 <= empty_idx < len(line) and line[empty_idx] == 0:
                    empty_idx += 2
                    
        if empty_idx>=index:  
            file = int(line[index])
            #print(f"\n{ID=},{index=},{file=},{empty_idx=}")
            #print(original_line)
            ans+=sum(ID*(i+sum(original_line[:index])) for i in range(file))
            #print(f"empty_idx>=index: adding {sum(ID*(i+sum(original_line[:index])) for i in range(file))} to ans")

        #print(line)
        #print(ans)
        #print("-" * 100)

print(ans)
print("Time taken:",time()-t0)

"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day13pt1.py (c) 2024
Desc: description
Created:  2024-12-13T05:40:44.071Z
Modified: 2024-12-13T06:21:46.588Z
"""

from time import time
import re


def solve_eqns(x1,y1,x2,y2,p1,p2):
    #find a2 value
    a2 = (p1*y1-p2*x1)/(x2*y1-x1*y2)
    #find a1 value
    a1 = (p1-a2*x2)/x1

    return a1,a2


t0=time()

ans=0
with open("input.txt", "r") as f:
    lines=f.readlines()
    for i in range(0,len(lines),4):
        
        x1,y1 = re.findall(r'\d+', lines[i])
        # print(f"{x1=}, {y1=}")
        x2,y2 = re.findall(r'\d+', lines[i+1])
        # print(f"{x2=}, {y2=}")
        p1,p2 = re.findall(r'\d+', lines[i+2])
        # print(f"{p1=}, {p2=}")
        x1,y1,x2,y2,p1,p2 = int(x1),int(y1),int(x2),int(y2),int(p1),int(p2)

        # print(f"{x1} a1+ {x2} a2 = {p1}")
        # print(f"{y1} a1+ {y2} a2 = {p2}")

        a1,a2 = solve_eqns(x1,y1,x2,y2,p1,p2)
        # print(f"{a1=}, {a2=}")
        # print(f"{x1} {a1}+ {x2} {a2} = {p1}")
        # print(f"{y1} {a1}+ {y2} {a2} = {p2}")

        if a1==int(a1) and a2==int(a2):    
            # print(a1*3+a2)
            ans+=a1*3+a2
        # print('-'*100)

print(ans)
print('Time taken:',time() - t0)